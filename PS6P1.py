quantity = int(input("Enter the quantity of widgets: "))

if quantity > 10000:
    price = 10.00
elif quantity >= 5000 and quantity <= 10000:
    price = 20.00
else:
    price = 30.00

extended_price = quantity * price


tax_rate = 0.07
tax_amount = extended_price * tax_rate


total_price = extended_price + tax_amount


print("Extended Price:", extended_price)
print("Tax Amount (7%):", tax_amount)
print("Total Price:", total_price)
