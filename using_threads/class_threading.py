from threading import Thread # this is a thread control object. The actual Thread belongs to the operating system
import random
import time

class MyClass():
    '''We will call this class on a separate thread.
    For this to work we must add a __call__ method to our class'''
    def __call__(self, n):
        '''loop over several iterations and sleep randomly'''#
        for i in range(0,6):
            print(f'{n} is working...')
            time.sleep(random.random()*0.1) # up to a tenth of a sec

def main():
    '''invoke the class in new threads'''
    c1 = MyClass() # we have an instance of the class
    t1 = Thread(target=c1, args=(1,))
    t2 = Thread(target=c1, args=(2,))
    t3 = Thread(target=c1, args=(3,))
    t1.start()
    t2.start()
    t3.start()
    # NB you need to start all you threads before trying to join any of them back
    t1.join()
    t2.join()
    t3.join()
    print('main thread')

if __name__ == '__main__':
    main()