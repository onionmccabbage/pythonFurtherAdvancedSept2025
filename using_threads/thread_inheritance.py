from threading import Thread
import time
import random

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
    for _ in range(0,16):
        thread_list.append( MyClass(_) )
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()
    print('back on the main thread')
    


if __name__ == '__main__':
    main()