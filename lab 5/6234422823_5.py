balance = 50000
while balance != 0 :
    withdraw = float(input("withdraw : "))
    if balance >= withdraw :
        balance = balance - withdraw
    else :
        print ("Insufficient fund.")
print ("Balance is 0.")