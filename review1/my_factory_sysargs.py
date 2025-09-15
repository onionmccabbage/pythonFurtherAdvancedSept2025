# we may need to manufacture related entities
# Here we will manufacture creatures

from abc import ABCMeta, abstractmethod
import sys

# we may declare an abstract class
class Animal(metaclass=ABCMeta):
    '''This abstract class contains no implmentation'''
    @abstractmethod
    def make_noise(self):
        pass

# we my then use this sbstrct class to create concrete implementations
class Dog(Animal): # this class inherits from our abstract class
    def make_noise(self):
        return 'woof'
class Cat(Animal):
    def make_noise(self):
        return 'miaow'
class Lion(Animal):
    def make_noise(self):
        return 'roar'
class Bat(Animal):
    def make_noise(self):
        return '______'
    
class CreatureFactory:
    '''This is a single-point-of-access to manufacture any type of creature avilable'''
    def make_sound(self, obj):
        # e.g. cat, lion etc
        return eval(obj)().make_noise() 
    def __str__(self):
        '''__str__ is used by print - we may override it'''  
    def __repr__(self):
        '''__repr__ is used in immediate mode (and in Jupyter)'''

if __name__ == '__main__':
    # Python will ALWAYS set sys.argv[0] to the name of the currently running module
    print(sys.argv) # there is always a list of system arguments (string)


    cf = CreatureFactory() # an instance of our factory
    
    # check to see if a 'creature' has already been provided as a system argument
    if len(sys.argv) > 1:
        # creature = input('Which creature: ')
        creature = sys.argv[1]
        if creature in ('Cat', 'Dog', 'Lion', 'Bat'):
            noise = cf.make_sound(creature) 
            print(f'The {creature} says {noise}')
        else:
            pass # we could raise an exception
