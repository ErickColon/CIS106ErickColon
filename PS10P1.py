def compute_next_month_sales(month, sales):
  forecast_percent = 0.0

  if month in ["Jan", "Feb", "Mar"]:
      forecast_percent = 0.10
  elif month in ["Apr", "May", "Jun"]:
      forecast_percent = 0.15
  elif month in ["Jul", "Aug", "Sep"]:
      forecast_percent = 0.20
  elif month in ["Oct", "Nov", "Dec"]:
      forecast_percent = 0.25

  next_month_sales = sales * (1 + forecast_percent)
  return next_month_sales

while True:
  user_input = input("Do you want to calculate next month's sales forecast? (Yes/No): ").strip().lower()

  if user_input == "no":
      break
  elif user_input == "yes":
      month = input("Enter the month (e.g., Jan, Feb, Mar): ").strip()
      sales = float(input("Enter the current month's sales: "))

      next_month_sales = compute_next_month_sales(month, sales)

      print("Next month's forecasted sales: ", next_month_sales)
  else:
      print("Invalid input. Please enter 'Yes' or 'No'.")
