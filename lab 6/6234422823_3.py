n = int(input("Enter integer : "))
cnt = 0
if n == 0 or n == 1 :
    print (n,"is not a prime.")
elif n == 2 :
    print (n,"is a prime.")
else :
    for i in range (1,n+1) :
        if n % i == 0 :
            cnt = cnt + 1
    if cnt > 2 :
        print (n,"is not a prime.")
    elif cnt == 2 :
        print (n,"is a prime.")