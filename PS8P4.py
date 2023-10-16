with open("order_data.txt", "r") as file:
    lines = file.readlines()

total_extended_price = 0 
order_count = 0  


current_item = ""
current_quantity = 0
current_price = 0


for line in lines:
    line = line.strip()  

    
    if not line:
        continue

    if not current_item:
        current_item = line
    elif current_quantity == 0:
        current_quantity = float(line)
    else:
        current_price = float(line)

        
        extended_price = current_quantity * current_price
        total_extended_price += extended_price

      
        print("Item:", current_item)
        print("Quantity:", current_quantity)
        print("Price: $", current_price)
        print("Extended Price: $", extended_price)
        print()

       
        current_item = ""
        current_quantity = 0
        current_price = 0

        order_count += 1


print("Sum of All Extended Prices: $", total_extended_price)
print("Number of Orders:", order_count)
if order_count > 0:
    average_order = total_extended_price / order_count
    print("Average Order: $", average_order)
else:
    print("No orders found.")
