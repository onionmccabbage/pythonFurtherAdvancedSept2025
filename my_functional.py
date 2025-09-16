# many people choose to write class-based code. We may also write function-based code
from random import randint

# functional design
def fnA(*args): # all the positional arguments will be gathered into a tuple called args
    '''we may choose to behave differently depending on how many arguments'''
    if len(args)==0:
        '''we have zero arguments...'''
        return 'default behaviour'
    if len(args)==1:
        '''we have a single argument'''
        return f'Value {args[0]} exists' # we would probably do some clever work here
    if len(args)>=2:
        return list(args) # converting the tuple into a list
    
# same can be done with keyword arguments
def fnB(**kwargs): # all teh keyword arguments will be gathered into a dict called kwargs
    return kwargs # here we simply return the dict
    
# pure functions can be entirely predicted - for given inputs we precicely know the outcome
# impure functions have side-effects we cannot predict (makes them a bit harder to test)

def fnRand():
    return randint(0,10) # we cannot predict the outcome of this function

if __name__ == '__main__':
    print(  fnA()  )
    print(  fnA(True)  )
    print(  fnA(3,4)  )
    print(  fnA('a', False, (3,2,1), {5,6,7,7,8})  )
    print(  fnB(x=7, h='hello', f=fnA, xxxyyy=True)   )
    # call our impure function
    print( fnRand() )