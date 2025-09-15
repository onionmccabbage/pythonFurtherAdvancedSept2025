# writing a custom context manager class (without using the contextlib)

import sys

class Redirect:
    '''This class will redirect output to a diferent stream
    When completed, the context will return to the original output stream'''
    # all Python classes include default life-cycle event handlers
    def __init__(self, new_stdout): # called ONCE every time this class is instantiated
        self.new_stdout = new_stdout
    def __enter__(self): # called every time we use an instance of this class
        self.original_stdout = sys.stdout # store the current context
        sys.stdout = self.new_stdout
    # __exit__ is called every time an instance completes its execution
    def __exit__(self, exc_type, exc_value, exc_traceback): # all these are required
        sys.stdout = self.original_stdout # return to the original context
    def __del__(self): # called ONCE when we delete an instance (or it goes out of contention)
        pass # often used for doing clean-up for this class

def main():
    '''exercise the code'''
    my_text = 'this will be redirected to a file instead of the console'
    fout = open('my_log.txt', 'at')
    r = Redirect(fout) # we pass a context in this case it is a file access object
    with r:
        print(my_text)
    fout.close()
    print('back to the console (default context)')

if __name__ == '__main__':
    main()