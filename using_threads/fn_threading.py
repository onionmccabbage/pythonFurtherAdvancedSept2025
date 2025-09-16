from threading import Thread
# in order to emulate long-running code we will use random and time libraries
import random
import time

def myFn(n):
    for i in range(0,6):
        print(f'{n} is working...')
        time.sleep( random.random()*0.1 ) # sleep for a fractino of a second

def main():
    '''invoke the functino on additional threads'''
    # NB fora tuple that contains a single value you MUST include a comma
    t1 = Thread(target=myFn, args=(1,)) # we target a function to run on a new thread
    t2 = Thread(target=myFn, args=(2,))
    t3 = Thread(target=myFn, args=(3,))
    t4 = Thread(target=myFn, args=(4,))
    # we may start the threads
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    #when does this line execute....
    print('from the main thread')
    # we often choose to pause the main thread until subthreads have completed
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    # when those other threads have completed, they will re-join this main thread, which then carries on
    print('all the subthreads have completed')
    # it is as good idea to tidy up when we no longer need other threads

if __name__ == '__main__':
    main()