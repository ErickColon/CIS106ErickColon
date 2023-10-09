num_students = 0

continue_program = input("Do you want to enter student data? (Enter 'Yes' to continue): ").strip().lower()

while continue_program == "yes":
    
    last_name = input("Enter last name: ")
    score1 = float(input("Enter the first exam score: "))
    score2 = float(input("Enter the second exam score: "))

  
    average_score = (score1 + score2) / 2

 
    print("Last Name:", last_name)
    print("Average Exam Score:", average_score)

   
    num_students += 1

   
    continue_program = input("Do you want to enter data for another student? (Enter 'Yes' to continue): ").strip().lower()

print("Total number of students entered:", num_students)
