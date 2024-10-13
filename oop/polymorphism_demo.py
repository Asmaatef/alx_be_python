import math
class Shape :
    def area(self):
        raise  NotImplementedError("derived classes need to override this method.") 
class Rectangle(Shape):
    def __init__(self ,length ,width):
       self.length = length
       self.width = width
    def area(self):
        return self.length * self.width
class Circle(Shape):
    def __init__(self ,raduis):
        self.raduis = raduis
    def area(self):
        return math.pi *(self.raduis **2)
