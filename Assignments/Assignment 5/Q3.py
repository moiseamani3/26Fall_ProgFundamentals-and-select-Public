def check_number(number):
   # return "even" if number % 2 == 0 else "odd"
   even = number % 2 == 0
   odd = not even
   return "even" if even else "odd"

number = int (input("enter a whole number"))

print(f"{number} is an {check_number(number)} number")









