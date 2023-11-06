def calculate_discount_percent(make, model, electric_vehicle_code):
  if make == "Honda" and model == "Accord":
      return 0.10
  elif make == "Toyota" and model == "Rav4":
      return 0.15
  elif electric_vehicle_code == "Y":
      return 0.30
  else:
      return 0.05

def calculate_out_the_door_price(msrp, make, model, electric_vehicle_code):
  discount_percent = calculate_discount_percent(make, model, electric_vehicle_code)
  new_msrp = msrp * (1 - discount_percent)
  total_price = new_msrp * 1.07  # Add 7% sales tax

  return total_price

total_msrp = 0
total_sales_price = 0

while True:
  user_input = input("Do you want to calculate the out-the-door price of an automobile? (Yes/No): ").strip().lower()

  if user_input == "no":
      break
  elif user_input == "yes":
      make = input("Enter the make of the automobile: ").strip()
      model = input("Enter the model of the automobile: ").strip()
      electric_vehicle_code = input("Is it an electric vehicle? (Y or N): ").strip().upper()
      msrp = float(input("Enter the MSRP (sticker price) of the automobile: "))

      total_price = calculate_out_the_door_price(msrp, make, model, electric_vehicle_code)

      total_msrp += msrp
      total_sales_price += total_price

      print("Out-the-door price of the automobile: $", total_price)
  else:
      print("Invalid input. Please enter 'Yes' or 'No'.")

print("Total MSRP of all automobiles: $", total_msrp)
print("Total sales price of all automobiles: $", total_sales_price)
