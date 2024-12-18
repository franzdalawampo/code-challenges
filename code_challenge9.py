for a in range(1,6):
  for b in range(6,a,-1):
    print(" ", end="")
  for c in range(1,a+1):
    print("*", end="")
  for d in range(1,a):
    print("*", end="")
  print()
for e in range(1,6):
  for f in range(1,e+1):
    print(" ", end="")
  for g in range(6,e+1,-1):
    print("*", end="")
  for h in range(6,e,-1):
    print("*", end="")
  print()