print("---------------------")
grocery=input("Hi! Did you do groceries today?(yes/no): ")

if grocery.lower() == "yes":
  print("Great! Lets continue the process.")
  senior=input("Are you a senior citizen? (yes/no): ")
  if senior.lower() == "yes":
    print("Okay, let's continue the process for your discount and payment.")
    seniorname=input("Please enter your name: ")
    print(f"Hi, {seniorname}.")
    seniorage=eval(input("Please enter your age: "))
    if seniorage >= 60 and seniorage <= 150:
      print("We're gonna charge you with 12.3% tax for the item/s you're buying.")
      print("But you're granted with the Senior Citizen Discount with 12.3% discount,\nand with items over 4000 pesos, you're also granted 3.8% discount.")
      item=input("What did you purchase today?: ")
      price=eval(input("Please input the price of the item/s: "))
      payment=eval(input("Enter your payment: "))
      #I used the same formula from the tax to the discount since it's the same value, though the discount deducts only the tax from item.
      taxbase = price * 0.123
      taxadded = price + taxbase
      sdiscount = taxadded - taxbase
      fourkdiscbase = price * 0.038
      fourkdiscadded = sdiscount - fourkdiscbase
      changenonfourk = payment - sdiscount
      changewithfourk = payment - fourkdiscadded
      print(f"The price of {item} is: {price} pesos")
      print(f"I receive {payment} pesos.")
      if (price <= 4000) :
        print(f"The total price of the {item} is {sdiscount} pesos.")
        print(f"Your change is {round(changenonfourk,2)} pesos.")
        print("Thank you for shopping?")
      elif (price >= 4001) :
        print(f"The total price of the {item} is {fourkdiscadded} pesos, you have saved {round(fourkdiscbase,2)} pesos. ")
        print(f"Your change is {round(changewithfourk,2)} pesos.")
        print("Thank you for shopping!")
      else:
        print("Thank you for shopping.")
    else:
      print("Invalid Age.")
  else:
    print("Okay, we'll continue to the normal process to non-senior citizens.")
    normalname=input("Please enter your name: ")
    print(f"Hi, {normalname}.")
    normalage=eval(input("Please enter your age: "))
    if (normalage <= 59):
      print("We're gonna charge you with 12.3% tax for the item/s you're buying.")
      print("We're also gonna be granting you with 3.8% discount for items over 4000 pesos.")
      itemnormal=input("What did you purchase today?: ")
      pricenormal=eval(input("Please input the price of the item/s: "))
      paymentnormal=eval(input("Enter your payment: "))
      taxbasenormal=pricenormal * 0.123
      taxaddednormal=pricenormal + taxbasenormal
      fourkdiscnormal=taxaddednormal * 0.038
      fourkdiscnormaladded=taxaddednormal - fourkdiscnormal
      normalchange=paymentnormal - taxaddednormal
      normalchangefourk=paymentnormal - fourkdiscnormaladded
      print(f"The price of {itemnormal} is: {pricenormal} pesos")
      print(f"I receive {paymentnormal} pesos.")
      if (pricenormal >= 4001):
        print(f"The total price of {itemnormal} is {round(fourkdiscnormaladded,2)} pesos.")
        print(f"You have saved {round(fourkdiscnormal,2)} pesos.")
        print(f"Your change is {round(normalchangefourk,2)} pesos.")
        print("Thank you for shopping!")
      elif (pricenormal <= 4000):
        print(f"The total price of {itemnormal} is {taxaddednormal} pesos.")
        print(f"Your change is {round(normalchange,2)} pesos.")
        print("Thank you for shopping!")
      else:
        print("Thank you for shopping.")
    else:
      print("Thank you for shopping.")
else:
  print("Do your groceries first to continue the process.")