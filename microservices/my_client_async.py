import asyncio

async def my_client(message):
    '''an asynchronous client to send a message to the server'''
    reader, writer = await asyncio.open_connection('localhost', 8888)
    print(f'Sending message {message}')
    # all communication is over http so we must encode everything
    writer.write(message.encode())
    await writer.drain() # useful for large data streams
    writer.close()
    reader.close()

if __name__ == '__main__':
    asyncio.run(my_client('message from client'))