def load_data_from_file(file_path):
  data = []
  with open(file_path, 'r') as file:
      for line in file:
          last_name, score = line.strip().split(',')
          data.append((last_name, int(score)))
  return data

def display_student_info(data):
  print("Student Information:")
  for last_name, score in data:
      print(f"Last Name: {last_name}, Score: {score}")

def display_highest_and_lowest(data):
  high_var = 0
  low_var = 999
  high_index = 0
  low_index = 0

  for i, (last_name, score) in enumerate(data):
      if score > high_var:
          high_var = score
          high_index = i
      if score < low_var:
          low_var = score
          low_index = i

  print("\nStudent with Highest Score:")
  print(f"Last Name: {data[high_index][0]}, Score: {data[high_index][1]}")

  print("\nStudent with Lowest Score:")
  print(f"Last Name: {data[low_index][0]}, Score: {data[low_index][1]}")

def main():
  file_path = "student_data.txt" 
  data = load_data_from_file(file_path)

  display_student_info(data)

  display_highest_and_lowest(data)

if __name__ == "__main__":
  main()
