# the factory design pattern: manufacture related entities
# here we will manufacture creatures

# abc stands for Abstract Base Class
from abc import ABCMeta, abstractmethod
class Animal(metaclass=ABCMeta):
    '''This abstract class contains no implementation'''
    @abstractmethod
    def make_noise(self):
        pass

# next we declare our concrete classes (often in other modules)
class Dog(Animal):
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
        return '_____'

