# There are many occasions where we need to manage thread locks
# we talk about 'thread safe' code, where data assets are reliably 
# exposed to a single thread at a time
import threading
import time
import random
import timeit

# here are some global variables
testsAvailable = 2048 # this would usually be a DB, an API, a file access...
lock = threading.RLock() # RLock is a re-entrant lock
num_runners = 256 # this is limited by the OS thread management

class TestRunner(threading.Thread): # NB here there will be no actual tests
    '''imitate random time between running tests across threads'''
    testsRun = 0
    def __init__(self, i):
        threading.Thread.__init__(self) # we tend to call this rather than super()
        self.lock = lock # we grab the global lock (we do not yet use it)
        self.i = i
        print(f'test Runner {self.i} starts running tests')
    def run(self):
        global testsAvailable
        running = True
        while running:
            self.randomDelay()
            self.lock.acquire() # we now have exclusive access to data, we acquired the global lock
            if testsAvailable <=0:
                running = False # stop running!
            else:
                testsAvailable -= 1
                self.testsRun  += 1
                # here we would run the test....
                # print(f'Test runner {self.i} runs a test')
            self.lock.release() # make the lock available for other threads
    def randomDelay(self):
        '''randomly sleep to emulate the time taken to run a test'''
        time.sleep(random.randint(0,4)/4) # 0, 0.25, 0.50, 0.75 as possible delays

# NB as with all code, any threads will be I/O bound

if __name__ == '__main__':
    tester_list = []
    start = timeit.default_timer()
    for _ in range(0,num_runners):
        tester = TestRunner(_)
        tester_list.append(tester)
        tester.start()
    # we do not have touse join but it is common practice
    for _ in tester_list:
        _.join()
    end = timeit.default_timer()
    print(f'total execution time: {end-start}')