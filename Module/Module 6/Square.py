import math
class Square:
    def __init__(self, the_side_length):
        self.height = the_side_length
    def area(self):
        return self.height * self.height 


car = Square(6)
print(f"The area of the square is: {car.area()}")
car.height = 10
print(f"The area of the square is: {car.area()}")
car.height = 25
print(f"The area of the square is: {car.area()}")

