num_tickets = int(input("Enter the number of concert tickets: "))

if num_tickets >= 25:
    price_per_ticket = 50.00
elif 10 <= num_tickets <= 24:
    price_per_ticket = 60.00
elif 5 <= num_tickets <= 9:
    price_per_ticket = 70.00
else:
    price_per_ticket = 75.00

total_cost = num_tickets * price_per_ticket

print("Number of Tickets:", num_tickets)
print("Price Per Ticket: $", price_per_ticket)
print("Total Cost: $", total_cost)
