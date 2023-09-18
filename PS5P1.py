#Input Phase 
quantity = float(input("Enter the quantity of the item: "))


if quantity >= 1000:
    unit_price = 3.00
else:
    unit_price = 5.00

#Process Phase

extended_price = quantity * unit_price


tax_percentage = 0.07
tax = extended_price * tax_percentage


total = extended_price + tax

#Output Phase 
print("Quantity: ", quantity)
print("Unit Price: $", unit_price)
print("Extended Price: $", extended_price)
print("Tax: $", tax)
print("Total: $", total)
