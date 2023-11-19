def display_names(names):
  print("Names:")
  for name in names:
      print(name)

def display_names_reverse(names):
  print("\nNames in Reverse Order:")
  for name in reversed(names):
      print(name)

def main():
 
  last_names = ["Sam", "erick", "Will", "Jones", "Barry", "Davis", "Miller", "Kyle", "Mason", "Tyler"]

  display_names(last_names)

  display_names_reverse(last_names)

if __name__ == "__main__":
  main()
