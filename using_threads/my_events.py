# we can use thread events
from threading import Thread, Event
import time

event = Event() # a global asset (nb thread events do not need to be global)

def fn(n):
    '''this function will be targeted by threads'''
    global event # each instance of this function will have access to the same global event object
    print(f'{n} is waiting')
    event.wait()
    print(f'{n} continuing after the event')

# We would trigger events to carry out communication
# - when an asset is ready (DB, API, file system..)
# - when the threads need to end (write some clean thread-ending code)
# - a heartbeat from the main thread
if __name__ == '__main__':
    '''exercise this module'''
    thread_l = [Thread(target=fn, args=(_,)) for _ in range(0,4)]
    for t in thread_l:
        t.start()
    time.sleep(3) # the main htrad will sleep a while
    event.set() # here the global event (on the main thread) send an event message to ALL threads
