def compute_averages(scores, handicap):
  average_score = sum(scores) / len(scores)
  average_score_with_handicap = average_score + handicap
  return average_score, average_score_with_handicap

def main():
  last_name = input("Enter bowler's last name: ")
  game_scores = []

  for i in range(3):
      score = float(input(f"Enter game score {i + 1}: "))
      game_scores.append(score)

  handicap = float(input("Enter bowler's handicap: "))

  average_score, average_score_with_handicap = compute_averages(game_scores, handicap)

  print("\nBowler Information:")
  print("Last Name: last_name", last_name)
  print("Average Score: average_score:", average_score)
  print("Average Score with Handicap: ", average_score_with_handicap)

if __name__ == "__main__":
  main()
