balance = 10000
amount=int(input("enter amount"))

if amount<=balance:
    if amount%100==0:
        print("transaction successful")
    else:
        print("enter amount in multiples of 100")
else:
    print("enter amount in multiple of 100")
