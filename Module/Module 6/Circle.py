#make sure to import the math module to use the value of pi or other mathematical functions.
import math

#create a class called Circle that takes the radius as an argument and has a method to calculate the area of the circle.
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2

#create an instance of the Circle class and print the area of the circle.
circle1 = Circle(5)
print(f"The area of the circle is: {circle1.area()}")