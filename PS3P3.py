#Input Phase
Mealtotal = float(input("Enter Meal Total $:"))

#Process Phase
tip_percent_15 = Mealtotal * .15
tip_percent_18 = Mealtotal * .18
tip_percent_20 = Mealtotal * .20

Total_with_tip_15 = tip_percent_15 + Mealtotal
Total_with_tip_18 = tip_percent_18 + Mealtotal
Total_with_tip_20 = tip_percent_20 + Mealtotal

#Output Phase
print("Total:", Mealtotal)
print("Tip:", tip_percent_15)
print("Total with Tip:", Total_with_tip_15)

print(" ")

print("Total:", Mealtotal)
print("Tip:", tip_percent_18)
print("Total with Tip:", Total_with_tip_18)

print(" ")

print("Total:", Mealtotal)
print("Tip:", tip_percent_20)
print("Total with Tip:", Total_with_tip_20)
