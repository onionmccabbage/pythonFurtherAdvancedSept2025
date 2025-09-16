class Point: # by default all classes inherit from object
    '''this class defines a point in 2-d space
    x and y will be coordinates tha uniquely define this point'''
    __slots__ = ['__x', '__y'] # restricted what properties are permitted
    def __init__(self, x, y):
        self.x = x # this line invokes the setter method for x
        self.y = y
    @property
    def x(self): # getter method
        return self.__x # this value is not accessible outside the class
    @x.setter
    def x(self, new_x):
        if type(new_x) in (float, int):
            self.__x = new_x
        else:
            raise TypeError('x must be a number')
    @property
    def y(self): # getter method
        return self.__y # this value is not accessible outside the class
    @y.setter
    def y(self, new_y):
        if type(new_y) in (float, int):
            self.__y = new_y
        else:
            raise TypeError('y must be a number')
    def __str__(self): # if we define __str__ then it will be used when we print instances of this class
        return f'Point is at x:{self.__x} y:{self.__y}'
    def __repr__(self): # if we define __repr__ hen it will be used in immediate mode python
        return f'Point is represented by x:{self.__x} y:{self.__y}'
        
if __name__ == '__main__':
    p1 = Point(3,4)
    # p2 = Point('3', '4')
    # we cannot access the mangled values __x or __y
    # but be careful. By default we inherited from 'object' and all 'objects' allow arbitrary properties
    p1.__x = 'wibblywoo' # daft
    print(p1.__x)
    print(p1)

