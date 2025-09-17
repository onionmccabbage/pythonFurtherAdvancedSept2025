# here we explore different approaches to generating the fibonacci sequence
# 1, 1, 2, 3, 5, 8, 13...

import timeit
from functools import reduce
from memory_profiler import profile
# to use cProfile
# python -m cProfile -o prof_out fib.py



@profile
def fib1(n):
    '''here is a low-performance fibonacci function'''
    if n in (0,1):
        return 1
    else:
        # recursively call this function
        return ( fib1(n-1) + fib1(n-2) )

@profile # invoke the memory profiler
def fib2(n):
    '''a more performant example'''
    seq = (0,1)
    for _ in range(2, n+2):
        seq += (reduce( lambda a,b: a+b, seq[-2:] ),) 
    return seq[-1] # return only the last member of the tuple

if __name__ == '__main__':
    start = timeit.default_timer()
    print( fib2(3) ) # fib1 about 0.02 or better. fib2 takes 0.0002 or better
    end = timeit.default_timer()
    print(end-start)
    
