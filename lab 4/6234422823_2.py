idNum = input("Enter student ID : ").strip()
lenght = len(idNum)

if lenght != 10 :
    print ("Invalid ID")
else :
    idNum = int(idNum)
    year = idNum//10**8
    if 48 <= year <= 62 :
        thirdDigit = (idNum//10**7)%10
        if thirdDigit == 3 or thirdDigit == 4 or thirdDigit == 7 :
            fac = idNum%100
            if 21 <= fac <= 40 or fac == 51 or fac == 53 :
                print ("Valid ID")
            else : print ("Invalid ID")
        else : print ("Invalid ID")
    else : print ("Invalid ID")
