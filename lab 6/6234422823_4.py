temp = float(input("Day 1 : "))
higherTemp = temp
for d in range (2,8) :
    temp = float(input("Day "+str(d)+" : "))
    if temp < higherTemp :
        print ("Temperature dropped on day",d)
    higherTemp = temp