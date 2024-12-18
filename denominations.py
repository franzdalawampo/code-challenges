deposit=eval(input("input your desired deposit amount: "))
print(f" your deposit amount of {deposit} represented in PH denominations is as follows: \n")
thousand=deposit//1000
thousandr=deposit%1000

fiveh=thousandr//500
fivehr=thousandr%500

twoh=fivehr//200
twohr=fivehr%200

oneh=twohr//100
onehr=twohr%100

fifty=onehr//50
fiftyr=onehr%50

twenty=fiftyr//20
twentyr=fiftyr%20

ten=twentyr//10
tenr=twentyr%10

five=tenr//5
fiver=tenr%5

one=fiver//1
oner=fiver%1

print(f"1000 - {thousand}")
print(f"500 - {fiveh}")
print(f"200 - {twoh}")
print(f"100 - {oneh}")
print(f"50 - {fifty}")
print(f"20 - {twenty}")
print(f"10 - {ten}")
print(f"5 - {five}")
print(f"1 - {one}")
