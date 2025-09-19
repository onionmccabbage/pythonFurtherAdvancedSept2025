import asyncio
# make use of our byte writer to persist request content
from file_writer import writeBytes

async def handleRequests(reader, writer):
    '''this server will expect requests from clients and send simple responses'''
    data = await reader.read(1024) # only the first bytes of the request
    message = 'default (can\'t convert from bytes)'
    try:
        message = data.decode() # try to convert the bytes to a string
    except UnicodeDecodeError as err:
        pass

    address = writer.get_extra_info('peername') # this will be procided by the write object
    print(f'Server received {message} from {address}')
    writeBytes(data) # write the original bytes
    if message.lower() in ('quit', 'end', 'terminate'):
        '''terminate the server'''

async def main():
    '''start the service'''
    server = await asyncio.start_server(handleRequests, 'localhost', 8888)
    print('Async Server is running')
    # as usual we need a mechanism to keep our server running (a run loop)
    async with server:
        await server.serve_forever()


if __name__ == '__main__':
    asyncio.run( main() )