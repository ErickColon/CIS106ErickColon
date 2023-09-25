#Input Phase
item = input("Enter the item (A or any other letter for B): ")
quantity = float(input("Enter the quantity: "))

#Process phase
if item == "A":
    unit_price = 10.00
else:
    unit_price = 20.00


extended_price = quantity * unit_price

#Output phase
print("Item:",  item)
print("Unit Price: $", unit_price)
print("Extended Price: $", extended_price)
