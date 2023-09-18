#Input Phase
fixed_cost = float(input("Enter Fixed cost"))
price_per_unit = float(input("Enter price per unit"))
cost_per_unit = float(input("Enter cost per unit"))

#Process Phase 
unit = price_per_unit - cost_per_unit
Break_even_point = fixed_cost/unit

#Output Phase
print("The Break even point is ", Break_even_point)