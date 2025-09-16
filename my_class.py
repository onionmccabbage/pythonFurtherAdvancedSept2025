class Point: # by default all classes inherit from object
    '''this class defines a point in 2-d space
    x and y will be coordinates tha uniquely define this point'''
    def __init__(self, x, y):
        self.x = x
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
    def __str__(self):
        return f'Point is at x:{self.__x} y:{self.__y}'
        
if __name__ == '__main__':
    p1 = Point(3,4)
    # p2 = Point('3', '4')
    print(p1)

