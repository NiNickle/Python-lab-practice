import random
n = int(input("Your guess : "))
r = random.randint(1,9)
while n != r :
    n = int(input("Your guess : "))
print ("Correct")