# Write a custom decorator

# functions may take any object as arguments. Including other functions
def showArgs(func):
    '''this function may be used as a decorator
    We will reveal all the positional and keyword arguments of the decorated function'''
    # * will unpack all the positional arguments
    # ** will unpack all the keyword arguments
    def newFunc(*args, **kwargs):
        '''expose the arguments'''
        print(f'''Running a function called {func.__name__}
The positional arguments are {args}
The keyword arguments are {kwargs}''')
        return func(*args, **kwargs) # make sure to execute the function being decorated
    return newFunc # the decorator returns a new function

# we will need some other functions to try our decorator with
@showArgs # we add the decorator functionality to an existing function
def squares(m,n):
    '''return a list of the square integers between two facets'''
    s = []
    for i in range(m,n):
        s.append(i*i)
    return s

@showArgs
def otherFn(x,y,z):
    '''do stuff...'''
    return x*y*z

if __name__ == '__main__':
    '''exercise this module'''
    result = squares(1, 11)
    result2 = squares(m=3, n=7)
    print(result, result2)
    # otherFn
    r1 = otherFn(4,5,6)
    r2 = otherFn(x=4,y=5,z=6)
    r3 = otherFn(4,5,z=6)
    r4 = otherFn(4,z=5,y=6)