def compute_commission_and_target(sales):
  commission_rate = 0.10 if sales > 100000 else 0.05
  commission = sales * commission_rate
  next_year_target = 0.05 * sales
  return commission, next_year_target

def main():
  last_name = input("Enter salesperson's last name: ")
  sales = float(input("Enter total sales: "))

  commission, next_year_target = compute_commission_and_target(sales)

  print("\nSalesperson Information:")
  print("Last Name: last_name", last_name)
  print("Commission: $commission:", commission)
  print("Next Year's Target: $next_year_target:", next_year_target)

if __name__ == "__main__":
  main()
