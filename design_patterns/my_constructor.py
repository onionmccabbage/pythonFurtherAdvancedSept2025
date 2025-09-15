# constructor design pattern
a = 4

class Coffee:
    def __init__(self, milk):
        self.milk = milk
    @property # this is the getter-method (accessor)
    def milk(self):
        return self.__milk # name-mangled property of the class
    @milk.setter # this is the setter-method (mutator)
    def milk(self, new_value):
        # we usually validate the incoming new value
        self.__milk = new_value

if __name__ == '__main__':
    '''exercise our module code'''
    flat_white = Coffee(None)
    cappucino  = Coffee(True)
