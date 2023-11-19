def display_student_info(last_names, exam_scores):
  print("Student Information:")
  for i in range(len(last_names)):
      print(f"Last Name: {last_names[i]}, Exam Score: {exam_scores[i]}")

def display_student_info_reverse(last_names, exam_scores):
  print("\nStudent Information in Reverse Order:")
  for i in range(len(last_names) - 1, -1, -1):
      print(f"Last Name: {last_names[i]}, Exam Score: {exam_scores[i]}")

def main():

  last_names = ["Erick", "Kyle", "Will", "Jones", "Nick", "Davis", "Miller", "Jack", "Santi", "Tyler"]

  exam_scores = [85, 92, 78, 95, 89, 88, 76, 90, 82, 94]

  display_student_info(last_names, exam_scores)

  display_student_info_reverse(last_names, exam_scores)

if __name__ == "__main__":
  main()
