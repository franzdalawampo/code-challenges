#import os
cont=True
nt=0
while cont==True:
  tri=input("Do you wish to create more triangles? (yes/no): ")
  if tri.lower()=="no":
    print("Loop has ended")
    break
    cont = False
  elif tri.lower()=="yes":
    #os.system('cls')
    nt+=1
    for b in range(1,7):
      for c in range(1,nt+1):
        for d in range(1,b+1):
          print("*", end=" ")
        for e in range(7,b,-1):
          print(" ", end=" ")
        print(end="")
      print()
    continue
  else:
    print("Invalid input.")
    print("Please type yes or no only.")
    continue