import asyncio
# we may listen out for sys.argv
import sys

async def my_client(message):
    '''an asynchronous client to send a message to the server'''
    # convert the incoming to bytes
    b = makeBytes(message)
    reader, writer = await asyncio.open_connection('localhost', 8888)
    print(f'Sending message {b}')
    # all communication is over http so we must encode everything
    writer.write(b)
    await writer.drain() # useful for large data streams
    writer.close()
    # reader.close()

def makeBytes(values):
    '''convert the  values to bytes'''
    b = bytes(values)
    return b

if __name__ == '__main__':
    if len(sys.argv) >1:
        msg = ' '.join(sys.argv[1:])
    else:
        msg = range(0,256)
    asyncio.run(my_client(msg))