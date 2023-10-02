part_number = int(input("Enter a part number: "))
quantity = input("Enter the quantity: "))

if part_number == 10 or part_number == 55:
  unit_price = 1.00
elif part_number == 99: 
  unit_price = 2.00
  elif part_number == 80 or part_number == 70:
    unit_price = 3.00
  else unit_price =5.00

total_cost = quantity * unit_cost


print("Part Number:", part_number)
print("Cost per Unit:", unit_cost)
print("Total Cost:", total_cost)
