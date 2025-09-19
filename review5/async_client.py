import asyncio
import sys

async def my_client(message):
    '''a simple asynchronous client
    send a message to the async server'''
    reader, writer = await asyncio.open_connection('localhost', 8889)
    print(f'Sending {message}')
    writer.write(message.encode()) # all communication over http needs to be encoded
    await writer.drain() # asynchronously wait until the writer has completed
    writer.close()

# a function to create encoded bytes
# The majority of computer files are not human readable - they are byte files
def makeBytes(values):
    # lets make some bytes
    b = bytes( values ) 
    print(b) # print will nicely format the bytes as text
    return b


def writeBytes(b):
    # persist these bytes into a file
    try:
        fout = open('bfile', 'ab') # 'w' will (over)write, 'b' for bytes
        fout.write(b)
        fout.close()
    except FileExistsError as err:
        print(f'File already exists {err}')
    except Exception as err:
        print(f'something went wrong {err}')

if __name__ == '__main__':
    if len(sys.argv)>1:
        m = sys.argv[1]
    else:
        m='people'
    asyncio.run(my_client(m))