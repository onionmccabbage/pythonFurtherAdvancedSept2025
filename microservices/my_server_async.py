import asyncio

async def handleRequests(reader, writer):
    '''this server will expect requests from clients and send simple responses'''
    data = await reader.read(1024) # only the first bytes of the request
    message = data.decode() # convert the bytes to a string
    address = writer.get_extra_info('peername') # this will be procided by the write object
    print(f'Server received {message} from {address}')
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