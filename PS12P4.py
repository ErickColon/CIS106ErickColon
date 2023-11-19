def load_data_from_file(file_path):
  data = []
  with open(file_path, 'r') as file:
      for line in file:
          last_name, batting_average = line.strip().split(',')
          data.append((last_name, float(batting_average)))
  return data

def display_player_info(player_data):
  print("Player Information:")
  for last_name, batting_average in player_data:
      print(f"Last Name: {last_name}, Batting Average: {batting_average}")

def search_and_display_player(player_data, search_last_name):
  for last_name, batting_average in player_data:
      if last_name.lower() == search_last_name.lower():
          print(f"\nPlayer Found:")
          print(f"Last Name: {last_name}, Batting Average: {batting_average}")
          return

  print(f"\nPlayer with Last Name '{search_last_name}' not found.")

def main():
  file_path = "player_data.txt"  
  player_data = load_data_from_file(file_path)

  display_player_info(player_data)

  while True:
      search_last_name = input("\nEnter a last name to search (or 'exit' to quit): ")
      if search_last_name.lower() == 'exit':
          break
      search_and_display_player(player_data, search_last_name)

if __name__ == "__main__":
  main()
