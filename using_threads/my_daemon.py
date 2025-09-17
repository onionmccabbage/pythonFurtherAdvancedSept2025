from threading import Thread
import time

# normal function
def standardFn():
    '''this will be invoked on a thread in the normal way'''
    print('standard thread starting')
    time.sleep(5)
    print('standard thread is done')

# daemon function
def daemonFn():
    '''this will be invoked as a daemon thread'''
    print('daemon thread is starting')
    while True:
        time.sleep(0.5)
        print('heartbeat...')
    print('daemon thread is done')


if __name__ == '__main__':
    '''exercise the code in this module'''
    st = Thread(target=standardFn)
    dt = Thread(target=daemonFn, daemon=True) # keep running until the main thread is done
    st.start()
    dt.start()
    st.join() # we wait for the standard thread

    # the main thread might have other stuff to do
    for _ in range(0, 10000):
        # print('...', end=', ')
        pass