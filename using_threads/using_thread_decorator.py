# we may need a tool to ensure functions or classes are made thread safe
from threading import Thread, Lock, RLock, Semaphore

lk = Lock() # or tis could be RLock or a Semaphore

def lock_a_method(meth):
    '''this function aims to lock any method passed in'''
    global lk
    def locked_method(self, *args, **kwargs):
        '''this will be a locked version of the passed-in method'''
        # try:
        already_locked = getattr(meth, '__is_locked', False)
        print(f'{meth} is {already_locked}')
        # except ValueError as err:
            # print(err)
        # except Exception:
            # lk.acquire()
            # result = meth(self, *args, **kwargs)
            # lk.release()
        if already_locked==False:
            with lk: # the lock gets applied here see https://www.pythontutorial.net/python-concurrency/python-threading-lock/
                # lk.acquire() # do not acquire() it is already acquired by 'with'
                # print('locking...')
                return meth(self, *args, **kwargs)
                # the lock will be automaticaly released when the 'with' operator is done
        else:
            return meth(self, *args, **kwargs)
    # we need to assign a sensible name to our new method
    # lock_a_method.__name__ = f'locked_{meth.__name__}'
    locked_method.__is_locked = True # place a flag to indicate this method can be locked
    return locked_method # this contains a lockable version of the original method, renamed acordingly

def make_thread_safe(cls, meth_list, lk): # we choose to pass in a class, a list of method of that class to be locked, and a lock instance
    '''iterate over methods of a class, applying thread-safe lock to each'''
    init = cls.__init__ # make a copy of the initializer method of the class
    def new_init(self, *args, **kwargs):
        init(self, *args, **kwargs) # call teh original initializer method
        self.__lock = lk
    cls.__init__ = new_init # replace the original init with this new one
    # we iterate over eahc method in the method list, applying our lock safe function
    for meth in meth_list:
        old_meth = getattr(cls, meth)
        new_meth = lock_a_method(old_meth) # a lockable version of the old method
        setattr(cls, meth, new_meth) # replace the original method with a lockable version
    return cls # the original class, but with lockable methods

def lock_a_class(meth_list, lk):
    '''use this as a decorator'''
    return lambda cls: make_thread_safe(cls, meth_list, lk)

# choose which methods of the 'set' should be made lockable
@lock_a_class(['add', 'remove', 'my_method'], lk)
class MySet(set):
    '''inherit from the 'set' object with custom methods'''
    def __init__(self, other_set):
        set.__init__(self, other_set) # call the initializer of the set class
    @lock_a_method # apply the decorator to just one method
    def my_method(self, new_value):
        '''this method only allows int values to be added'''
        if type(new_value)==int:
            super().add(new_value)
        else:
            print('not an int')
            pass # do nothing

if __name__ == '__main__':
    '''exercise the module'''
    s = (1,2,3,4)
    m = MySet(s)
    m.add(5)
    m.remove(2)
    m.my_method(42)
    m.my_method('42') # nothing will happen
    print(m)
    # check stuff
    print(m.my_method.__is_locked) # True
    print(m.add.__is_locked) # True
    print(m.remove.__is_locked) # True