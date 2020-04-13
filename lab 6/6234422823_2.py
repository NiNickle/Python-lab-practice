n = int(input("Enter integer : "))
print (n,"is devisible by:")

for i in range (1,n+1) :
    if n % i == 0 :
        print (i)