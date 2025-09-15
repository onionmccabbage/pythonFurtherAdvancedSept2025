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

class CreatureFactory():
    '''This is a single-point-of-access to manufacture any type of creature'''
    def make_sound(self, obj):
        # e.g. cat, lion etc.
        # NB the 'eval' concept is generally considered poor form, we try to avoid it
        # this often considerd to be a security attack surface
        return eval(obj)().make_noise() # we might pass in a function or a class then find the __name__
    
if __name__ == '__main__':
    # exercise the code to make sure this module works as intended
    cf = CreatureFactory()
    n1 = cf.make_sound('Lion')
    print(n1)
    # a tuple of creatures
    cre = ('Cat', 'Bat', 'Dog', 'Cat', 'Lion')
    for _ in cre:
        print(f'{_} says {cf.make_sound(_)}')
