total_gross_pay = 0
employee_count = 0

continue_program = input("Do you want to enter employee data? (Enter 'Yes' to continue): ").strip().lower()

while continue_program == "yes":
    
    last_name = input("Enter employee's last name: ")
    hours_worked = float(input("Enter hours worked: "))
    rate_of_pay = float(input("Enter rate of pay: "))

    if hours_worked > 40:
        gross_pay = 40 * rate_of_pay + (hours_worked - 40) * (rate_of_pay * 1.5)
    else:
        gross_pay = hours_worked * rate_of_pay

    print("Last Name:", last_name)
    print("Gross Pay:", gross_pay)

    total_gross_pay += gross_pay
    employee_count += 1

    continue_program = input("Do you want to enter data for another employee? (Enter 'Yes' to continue): ").strip().lower()

print("Total Gross Pay:", total_gross_pay)
print("Number of Employees:", employee_count)

if employee_count > 0:
    average_pay = total_gross_pay / employee_count
    print("Average Pay:", average_pay)
else:
    print("No employee data entered.")
