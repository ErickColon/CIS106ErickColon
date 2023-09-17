#Input Phase
pricepershare = float(input("Enter Price per share: "))
Currentstock = float(input("Enter Current stock price: "))
Quantityofstock = float(input("Enter Quantity of stock"))

#Process Phase
Process = Currentstock - pricepershare
Value = Process * Quantityofstock

#Output Phase
print("The Value is $", Value)