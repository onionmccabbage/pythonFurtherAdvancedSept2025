# we may need a tool to ensure functions or classes are made thread safe
from threading import Thread, Lock, RLock, Semaphore

lk = Lock() # or tis could be RLock or a Semaphore

def lock_a_method(meth):
    '''this function aims to lock any method passed in'''
    global lk
    def locked_method(self, *args, **kwargs):
        '''this will be a locked version of the passed-in method'''
        try:
            already_locked = getattr(meth, '__is_locked')
        except ValueError as err:
            print(err)
        except Exception:
            # lk.acquire()
            # # print('locking...')
            # result = meth(self, *args, **kwargs)
            # lk.release()
            with lk: # the lock gets applied here see https://www.pythontutorial.net/python-concurrency/python-threading-lock/
                # lk.acquire()
                return meth(self, *args, **kwargs)
            # the lock will be automaticaly released when the 'with' operator is done
    # we need to assign a sensible name to our new method
    lock_a_method.__name__ = f'locked_{meth.__name__}'
    locked_method.__is_locked = True # place a flag to indicate this method can be locked
    return locked_method # this contains a lockable version of the original method, renamed acordingly

def make_thread_safe():
    '''iterate over methods of a class, applying thread-safe lock to each'''

def lock_a_class():
    '''use this as a decorator'''

class MySet(set):
    '''inherit from the 'set' object with custom methods'''
    def __init__(self, other_set):
        set.__init__(self, other_set) # calll the initializer of the set class
    @lock_a_method # apply the decorator to just one method
    def my_method(self, new_value):
        '''this method only allows int values to be added'''
        if type(new_value)==int:
            super().add(new_value)
        else:
            pass # do nothing



if __name__ == '__main__':
    '''exercise the module'''
    s = (1,2,3,4)
    m = MySet(s)
    m.add(5)
    m.my_method(42)
    m.my_method('42') # nothing will happen
    print(m)