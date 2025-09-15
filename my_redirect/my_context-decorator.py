# we can write a decorator function to implement redirection
# many Python operatins are I/O bound
# they are restricted by the speed of input and output
# remember - all I/O is carried out by the operating system on behalf of Python

# Redirection is the choice of where we get input or send output
# we may redirect output to 
# (e.g.) the console, a text or byte file, a spreadsheet, a DB, a log file an API a micro-service
# the standard output is known as sys.stdout by default this sends output to the console

from contextlib import contextmanager
import sys

@contextmanager
def outputRedirect(newOutputStream):
    '''redirect output to a new context'''
    old_sto = sys.stdout # store the current context
    sys.stdout = newOutputStream # set teh default output to a new context
    yield
    sys.stdout = old_sto # recover the original context

def main():
    '''execise the code to check it works as expected'''
    print('Using the default context')
    with open('my_log.txt', 'at') as fobj: # append text
        with outputRedirect(fobj): # or pass in any other context (DB, log, API etc)
            print('this output will be redirected')
    print('Back to the original context')

if __name__ == '__main__':
    main()