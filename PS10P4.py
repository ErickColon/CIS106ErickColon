def calculate_ticket_price(miles_from_downtown):
    if miles_from_downtown >= 30:
        return 12
    elif 20 <= miles_from_downtown <= 29:
        return 10
    elif 10 <= miles_from_downtown <= 19:
        return 8
    else:
        return 5

total_ticket_price = 0

while True:
    user_input = input("Do you want to calculate the train ticket price? (Yes/No): ").strip().lower()

    if user_input == "no":
        break
    elif user_input == "yes":
        last_name = input("Enter your last name: ").strip()
        miles_from_downtown = int(input("Enter the miles from downtown Chicago: "))

        ticket_price = calculate_ticket_price(miles_from_downtown)

        total_ticket_price += ticket_price

        print(f"Ticket price for {last_name}: ${ticket_price}")
    else:
        print("Invalid input. Please enter 'Yes' or 'No'.")

print("Total price of all tickets: $", total_ticket_price)
