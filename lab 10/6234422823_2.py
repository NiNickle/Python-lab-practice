Drink=["cappuccino","espresso","latte"]
Size=["S","L","s","l"]
x=1
total=0
cost={(1,1):60,(1,2):70,(2,1):45,(2,2):50,(3,1):65,(3,2):75}
while x!=0:
    Set=input("Enter drink, size and number : ")
    if Set=="exit":
        break
    drink,size,num=Set.lower().strip().split()
    if drink not in Drink:
        print("Drink not available.")
        continue
    if size not in Size:
        print("Incorrect size.")
        continue
    if drink == "cappuccino": x=1
    elif drink=="espresso": x=2
    elif drink=="latte": x=3
    if size == "S" or size == "s":y=1
    elif size == "L" or size == "l":y=2
    total+=(cost[x,y]*int(num))
print("Total : ",total)
