café_name = "Ikaze Café"
tax_rate = 0.08

menu = {
    "espresso": 3.00,
    "latte": 4.50,
    "cappuccino": 4.25,
    "mocha": 5.00,
    "muffin": 2.50,
    "croissant": 3.25,
}

order = []


#Prints a welcome message with the café name and the customer's name, using an f-string.
def greet(name):
    print(f"Welcome to {café_name}, {name}!")

#Loops through menu.items() and prints every item with its price.
def show_menu(menu):
    print()
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")
    
        

#If the order is empty, prints "Your order is empty." Otherwise prints each item with its price, then the number of items using len().
def show_order(order, menu):
    if not order:
        print("Your order is empty.")

    else:
        print("--- YOUR ORDER ---")
        for item in order:
            print(f"{item}: ${menu[item]:.2f}")
        print(f"Items: {len(order)}")


#Loops through the order, adds up each item's price from the menu, and returns the total.
def calculate_subtotal(order, menu):
    subtotal = 0.0
    for item in order:
        subtotal += menu[item]
    return subtotal

#Returns the discount in dollars, using the discount rules below.
def get_discount(subtotal, is_member):
    if is_member and subtotal >= 20:
        return subtotal * 0.15

    elif is_member and subtotal >= 10:
        return subtotal * 0.10

    elif not is_member and subtotal >= 25:
        return subtotal * 0.05

    else:
        return 0.0
    

#Calls calculate_subtotal() and get_discount(), works out tax and the total, and prints the receipt.
def print_receipt(name, order, menu, is_member):

    subtotal = calculate_subtotal(order, menu)
    discount = get_discount(subtotal, is_member)
    discounted_subtotal = subtotal - discount
    tax = discounted_subtotal * tax_rate
    total = discounted_subtotal + tax
    
    print(f"===== {café_name} RECEIPT =====")
    print(f"Customer: {name}")
    for item in order:
        print(f"{item}: ${menu[item]:.2f}")

    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discount: -${discount:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total: ${total:.2f}")


    if not is_member:
        print("Join our rewards club to earn discounts!")

    print(f"Thanks for visiting, {name}!")

    
##---MAIN PAGE---
          
print(f"*** {café_name} ***")

CustomerName = input("What is your name ?")
greet(CustomerName)

member_input = input("Are you a rewards member? (yes/no)").lower()
is_member = member_input == "yes"




while True:
    print()
    print("1. View menu")
    print("2. Add an item")
    print("3. Remove an item")
    print("4. View my order")
    print("5. Checkout")
    print()

    choice = input("Please choose a number from (1-5)") 
    #show_menu(choice)

    if choice == "1":
        print()
        show_menu(menu)

    elif choice == "2":
        item = input("What would you like?").lower()

        A = "espresso"
        B = "latte"
        C = "cappuccino"
        D = "mocha"
        E = "muffin"
        F = "croissant"

        #item_choice = input("Choose an option (1-6):")

        if item in menu:
            quantity = int(input("How many?"))

            if quantity >= 1:
                for qty in range(quantity):
                    order.append(item)
                print(f"Added {quantity} {item} to your order.")
            else:
                print("Quantity must be at least 1.")

        else:
            print(f"sorry, {item} is not on the menu.")




    elif choice == "3":

        item = input("Which item should I remove?").lower()

        if item in order:
            order.remove(item)
            print(f"Removed one {item}.")

        else:
            print(f"{item} isn't in your order.")


        
    elif choice == "4":
        show_order(order, menu)


    elif choice == "5":
        if len(order) == 0:
            print("Your order is empty. Please add something first.")

        else:
            print_receipt(CustomerName, order, menu, is_member)
            break

    else:
        print("Please choose a number from 1 to 5.")
        break



    
##    elif choise == "4":
##        print("--- YOUR ORDER ---")
##        print(3)

    
    

    


        


        
            

        
            
        
    

    


 

    
