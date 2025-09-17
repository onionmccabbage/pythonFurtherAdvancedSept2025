# here we explore different approaches to generating the fibonacci sequence
# 1, 1, 2, 3, 5, 8, 13...

import timeit
from memory_profiler import profile

def fib1(n):
    '''here is a low-performance fibonacci function'''
    if n in (0,1):
        return 1
    else:
        # recursively call this function
        return ( fib1(n-1) + fib1(n-2) )
    
if __name__ == '__main__':
    start = timeit.default_timer()
    print( fib1(28) )
    end = timeit.default_timer()
    print(end-start)
    
