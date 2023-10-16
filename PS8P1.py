p = float(input("Enter Principle"))
r = float(input("Enter rate"))
totint = 0.0
print("Year     Beginning Balence     End Balence")


for  x in range(1, 6, 1):
  i = p * r
  totint = totint + i
  endbal = p + i
  print(x, "     " , p, "     " , endbal)
  p = endbal
print("Total Interest Earned", totint)