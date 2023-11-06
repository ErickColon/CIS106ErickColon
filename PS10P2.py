def compute_square_footage(length, width, height):
  floor_ceiling_area = 2 * length * width
  wall1_area = 2 * length * height
  wall2_area = 2 * width * height
  total_area = floor_ceiling_area + wall1_area + wall2_area
  return total_area

while True:
  user_input = input("Do you want to calculate the number of gallons needed to paint a room? (Yes/No): ").strip().lower()

  if user_input == "no":
      break
  elif user_input == "yes":
      length = float(input("Enter the length of the room in feet: "))
      width = float(input("Enter the width of the room in feet: "))
      height = float(input("Enter the height of the room in feet: "))

      square_footage = compute_square_footage(length, width, height)
      gallons_needed = square_footage / 50

      print("Total square footage of the room:", square_footage)
      print("Number of gallons needed to paint the room:", gallons_needed)
  else:
      print("Invalid input. Please enter 'Yes' or 'No'.")
