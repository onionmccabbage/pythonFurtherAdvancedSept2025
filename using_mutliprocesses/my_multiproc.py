# we can invoke code to run in new Python processes
# each new process has its own copy of Python (and its own memroy etc)
# NB it is near impossible to communicate across multi processes
# most features are very similar to using multithreading
import os
import time
import multiprocessing

# it is far more common to use threading (or asyncio) rather than processing


def myFn(n):
    '''we will run this function in a separate process'''
    time.sleep(2)
    print(f'{n} is running in a separate process {os.getpid()}')



if __name__ == '__main__':
    print( os.cpu_count() ) # e.g. 2, 4, 8, 16, 32 .... these are discrete processing cores on the CPU
    print(f'The main process is running on {os.getpid()}')
    pl = [ multiprocessing.Process(target=myFn, args=(p, ))  for p in range(8) ]
    # next we start our processes
    for p in pl:
        p.start()
    # we may choose to join them also (often we do)
    done = [ p.join for p in pl ] # we could use a conventional iteration loop
