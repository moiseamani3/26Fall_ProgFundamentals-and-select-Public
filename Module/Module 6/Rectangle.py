import math

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width


rectangle1 = Rectangle(8, 15)
print(f"The area of the rectangle is: {rectangle1.area()}")
    