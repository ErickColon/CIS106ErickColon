principle = float(input("Enter the principle amount: "))
years_to_maturity = int(input("Enter the years to maturity: "))


if principle > 100000:
    interest_rate = 0.06
elif 50000 <= principle <= 100000:
    if years_to_maturity == 10:
        interest_rate = 0.05
    elif years_to_maturity == 5:
        interest_rate = 0.04
    else:
        interest_rate = 0.02
else:
    interest_rate = 0.02


first_year_interest = principle * interest_rate

print("Principle Amount:", principle)
print("Interest Rate:", interest_rate * 100, "%")
print("Interest Amount for the First Year:", first_year_interest)
