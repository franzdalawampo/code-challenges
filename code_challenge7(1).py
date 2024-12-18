#Simple Point-of-Sales Program with Senior Citizen discount

name=input("Hi! Please enter your name: ")
grocery=input("Did you do grocery today?(yes/no): ")

if grocery.lower() == "yes":
    print("Great! Let's continue the process.")
    senior=input("Are you a senior citizen?(yes/no): ")
    if senior.lower() == "yes" :
        print("Okay, let's continue the process for your discount and payment.")
        age=eval(input("How old are you?: "))
        if age >=60 and age <=150:
            print("We're gonna give you a 12.3 percent discount to your purchase today.")
            item1=input("What did you purchase today?: ")
            print(f"You have purchased {item1}.")
            
        else :
            print("Invalid Age.")    
    else :
        print("Okay, we'll continue to the normal process for non senior citizens.")
        normalage=eval(input("How old are you?: "))
        if normalage >=18 and normalage <= 59 :
            print("We're gonna charge you with the 12.3% tax from the item/s you purchased.")
            item2=input("What did you purchase today?: ")
            print(f"You have purchased {item2}.")
        else :
            print("Too young to get taxed hahaha.")       
    #age=eval(input("How old are you?: "))
    #if age >=60 and age <= 150 :
        #print("We're gonna give you a 12.3 percent discount to your purchase today.")
    #elif (age >=150) :
        #print("Invalid Age.")  
    #else:
        #print("We're gonna charge you with the 12.3% tax from the item/s you purchased.")
        #item=input("What did you purchase today?: ")
        #print(f"You have purchased {item}.")
        #payment=eval(input("Please enter your payment: ")
        #tax= payment * 0.123
        #4kdiscount= 0.038
        #taxadded= payment + tax
        #4kdiscountapplied= payment - 4kdiscount
        #discount= payment * 0.123
        #discountapplied= payment - discount
        #discountover4k= taxadded - 4kdiscount
        #if payment 
        #print("Your money is", payment ,"pesos, and you have saved, ",discount, "pesos.")
else :
    print("Do groceries first to continue the process, thanks.") 
   