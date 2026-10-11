def rectangle_stats(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

length = int(input("Enter the length in cm : "))
width = int(input("Enter the width in cm: "))

area, perimeter = rectangle_stats(length, width)

print(f"The area of the rectangle is {area:.2f} cm") 
print(f"The perimeter of the rectangle is {perimeter:.2f} cm")

    
    
