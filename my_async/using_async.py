# async stands for asynchronous i.e. out-of-time
# asyncio reminds us that the most common delays are I/O bound operations
# the aim of asyncio is to follow modern design practices with elegant code to handle these problems
import asyncio


# async-await is a common pattern in many modern languages
async def countA():
    '''emulate a long-running process'''
    print('first do this...')
    await asyncio.sleep(2) # or we could use time.sleep()
    print('then do that')

async def countB(): # typically a different function
    '''emulate a long-running process'''
    print('first do this...')
    await asyncio.sleep(2) # or we could use time.sleep()
    print('then do that')

async def main():
    '''run our I/O bound operations (or other long-tail functionality)'''
    await countA()
    await countB()


if __name__ == '__main__':
    asyncio.run( main() ) #use the async library to run our main function