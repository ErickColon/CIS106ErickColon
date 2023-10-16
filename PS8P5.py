with open("student_data.txt", "r") as file:
    lines = file.readlines()

total_tuition_owed = 0  
student_count = 0  


current_last_name = ""
current_district_code = ""
current_credits_taken = 0

in_district_cost_per_credit = 250.00
out_of_district_cost_per_credit = 500.00


for line in lines:
    line = line.strip()  

    
    if not line:
        continue

    if not current_last_name:
        current_last_name = line
    elif not current_district_code:
        current_district_code = line
    else:
        current_credits_taken = int(line)

        
        if current_district_code == "I":
            cost_per_credit = in_district_cost_per_credit
        else:
            cost_per_credit = out_of_district_cost_per_credit

      
        tuition_owed = current_credits_taken * cost_per_credit
        total_tuition_owed += tuition_owed

        print("Last Name:", current_last_name)
        print("Credits Taken:", current_credits_taken)
        print("Tuition Owed: $", tuition_owed)
        print()

       
        current_last_name = ""
        current_district_code = ""
        current_credits_taken = 0

        student_count += 1

print("Sum of All Tuition Owed: $", total_tuition_owed)
print("Number of Students:", student_count)
