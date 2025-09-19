import asyncio
from swapi_service import SwapiService

# we use async and await together
async def handleRequests(reader, writer):
    '''This server will expect to receive requests from clients
    Responses will be simple'''
    data = await reader.read(1024) # read in the first 1024 bytes from the incoming data stream
    message = data.decode() # convert the bytes to a string
    addr = writer.get_extra_info('peername')
    print(f'Received {message} from {addr}')
    # additional features
    # call Swapi Service
    swapi_instance = SwapiService()
    # do we have a permitted number (as a string)?
    if message in ('1','2','3','4','5','6','7'):
        response = swapi_instance.getSwapi('people', message)
    else:
        response = swapi_instance.getSwapi(message, 1)
    print(response)
    # commit every message received to a byte file
    writeBytes(data)

def writeBytes(n):
    '''persist n in a byte file'''
    print(f'writing {n} to byte file')
    # we need a file access object
    with open('my_byte_log', 'ab') as fout: # 'a' will append 'b' for bytes (default is 't' for text)
        if type(n) == bytes:
            fout.write(n)
        elif type(n) == str:
            fout.write(n.encode())
        fout.write(b'\n') # a new line character as a byte string

async def main():
    '''start the microservice server'''
    server = await asyncio.start_server(handleRequests, 'localhost', 8889) # localhost is 127.0.0.1
    print('Server started')
    # the server needs to run endlessly
    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run( main() )