def compute_exam_stats(scores):
  total_points = sum(scores)
  average_score = total_points / len(scores)
  return total_points, average_score

def main():
  last_name = input("Enter student's last name: ")
  exam_scores = []

  for i in range(3):
      score = float(input(f"Enter exam score {i + 1}: "))
      exam_scores.append(score)

  total_points, average_score = compute_exam_stats(exam_scores)

  print("\nStudent Information:")
  print(f"Last Name: last_name", last_name)
  print("Total Points: total_points", total_points)
  print("Average Exam Score: average_score:", average_score)

if __name__ == "__main__":
  main()
