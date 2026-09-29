name = "macbook"
unit_price = 1500
quantity = 3

tax_rate = 5/100

the_subtotal = unit_price*quantity
The_tax_amount = the_subtotal*0.05
The_final_total = the_subtotal+tax_rate

print(f"the_subtotal:{the_subtotal:.2f}")
print(f"The_tax_amount:{The_tax_amount:.2f}")
print(f"The_final_total:{The_final_total:.2f}")
