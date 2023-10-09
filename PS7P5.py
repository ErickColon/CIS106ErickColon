total_discount = 0


continue_program = input("Do you want to enter an order? (Enter 'Yes' to continue): ").strip().lower()


while continue_program == "yes":
  
    quantity = int(input("Enter the quantity of the item: "))
    price = float(input("Enter the price of the item: "))

   
    extended_price = quantity * price

   
    if extended_price > 10000.00:
        discount_percent = 0.25
    else:
        discount_percent = 0.10

    
    discount_amount = extended_price * discount_percent

   
    total = extended_price - discount_amount

   
    print("Extended Price:", extended_price)
    print("Discount Amount:", discount_amount)
    print("Total:", total)

    total_discount += discount_amount

   
    continue_program = input("Do you want to enter another order? (Enter 'Yes' to continue): ").strip().lower()


print("Total of all Discounts:", total_discount)
