for a in range(1,6):
  for b in range(6,a,-1):
    print(" ", end="")
  for c in range(1,a+1):
    print("*", end="")
  for d in range(1,a):
    print("*", end="")
  print()
for e in range(1,6):
  for d in range(6-2):
    print(" ", end="")
  for f in range(2):
    print("*", end="")
  print()
    
