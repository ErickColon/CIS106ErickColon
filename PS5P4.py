#Input Phase
appliance_name = input("Enter the name of the appliance: ")
appliance_cost = float(input("Enter the cost of the appliance: "))

#Process Phase
if appliance_cost > 1000.00:
  
  warranty_cost = 0.10 * appliance_cost
else:
    warranty_cost = 0.05 * appliance_cost

total_cost = appliance_cost + warranty_cost

#Output Phase 
print("Name of Appliance: ", appliance_name)
print("Cost of Appliance: $", appliance_cost)
print("Cost of Warranty: $", warranty_cost)
print("Total Cost: $", total_cost)
