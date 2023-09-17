#Input Phase
first_exam_score = float(input("Enter the score for the first exam: "))
second_exam_score = float(input("Enter the score for the second exam: "))


weight_first_exam = 0.60
weight_second_exam = 0.40

#Process Phase 
weighted_first_exam_score = first_exam_score * weight_first_exam
weighted_second_exam_score = second_exam_score * weight_second_exam


total_score = weighted_first_exam_score + weighted_second_exam_score

#Output phase
print(f"The total score is: {total_score}")
