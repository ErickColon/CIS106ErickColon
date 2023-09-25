#Input phase
num_books = float(input("Enter the number of books to order: "))
cost_per_book = float(input("Enter the cost per book: "))

#Process Phase
order_total = num_books * cost_per_book


if order_total > 50.00:
    shipping_charge = 0.00
else:

    shipping_charge = 25.00

#Output Phase
print("Order Total: $", order_total)
print("Shipping Charge: $", shipping_charge)
