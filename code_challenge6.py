#Age Categorizer
name=input("Please enter your name: ")
age=eval(input("Please enter your age: "))

if age>=1 and age<=8 :
    print(f"Hi {name}, your age is at the Toddler category.")
elif age>=9 and age<=14 :
    print(f"Hi {name}, your age is at the Pre-Teen category.")
elif age>=15 and age<=18 :
    print(f"Hi {name}, your age is at the Teenager category.")
elif age>=19 and age<=27 :
    print(f"Hi {name}, your age is at the Adulthood category.")
elif age>=28 and age<=44 :
    print(f"Hi {name}, your age is at the Middle Age category.")
elif age>=45 and age<=59 :
    print(f"Hi {name}, your age is at the Past Adulthood category.")
elif age>=60 and age<=150 :
    print(f"Hi {name}, your age is at the Senior Citizen category.")
else :
    print("Invalid Age")        
       
    