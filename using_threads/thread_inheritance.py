from threading import Thread
import time
import random
# use timeit for accurate timing
import timeit

class MyClass(Thread): # we inherit from the Thread class
    '''to use a clas inheriting from Threadwe must include a run method'''
    def __init__(self, n):
        Thread.__init__(self)
        self.n = n
    def run(self):
        for i in range(0,6):
            print(f'{self.n} is working...')
            time.sleep(random.random()*0.1)

def main():
    '''invoke the class as a Thread'''
    # we can work with a large quantity of new threads
    thread_list = []
    for _ in range(0,1024):
        thread_list.append( MyClass(_) )
    start = timeit.default_timer()
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()
    end = timeit.default_timer()
    # NB most of the time is spent with I/O bound operations such as 'print'
    print(f'total execution time: {end-start}')
    

if __name__ == '__main__':
    main()