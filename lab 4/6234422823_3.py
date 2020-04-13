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
                if  fac == 21 or fac == 23 or fac == 25 or \
                    fac == 28 or fac == 30 or fac == 31 or \
                    fac == 32 or fac == 33 or fac == 35 or \
                    fac == 36 or fac == 37 or fac == 38 or \
                    fac == 39 or fac == 53 : 
                    if thirdDigit == 7 :
                        sem = int(input("Enter semester : "))
                        if sem == 1 or sem == 2 :
                            if 48 <= year <= 49  :
                                    print ("Registration fee : 22,500")
                            elif 50 <= year <= 55 :
                                    print ("Registration fee : 26,000")
                            else : 
                                    print ("Registration fee : 31,000")
                        elif sem == 3 :
                            if 48 <= year <= 49  :
                                    print ("Registration fee : 6,000")
                            elif 50 <= year <= 55 :
                                    print ("Registration fee : 7,000")
                            else : 
                                    print ("Registration fee : 7,750")
                        else : print ("Invalid semester")
                    else :
                        sem = int(input("Enter semester : "))
                        if sem == 1 or sem == 2 :
                            if 48 <= year <= 49  :
                                    print ("Registration fee : 16,000")
                            elif 50 <= year <= 55 :
                                    print ("Registration fee : 18,000")
                            else : 
                                    print ("Registration fee : 21,000")
                        elif sem == 3 :
                            if 48 <= year <= 49  :
                                    print ("Registration fee : 4,000")
                            elif 50 <= year <= 55 :
                                    print ("Registration fee : 4,500")
                            else : 
                                    print ("Registration fee : 5,250")
                        else : print ("Invalid semester")
                if  fac == 22 or fac == 24 or fac == 26 or \
                    fac == 27 or fac == 29 or fac == 34 or \
                    fac == 40 or fac == 51 :
                    if thirdDigit == 7 :
                        sem = int(input("Enter semester : "))
                        if sem == 1 or sem == 2 :
                            if 48 <= year <= 49  :
                                    print ("Registration fee : 16,500")
                            elif 50 <= year <= 55 :
                                    print ("Registration fee : 19,000")
                            else : 
                                    print ("Registration fee : 23,000")
                        elif sem == 3 :
                            if 48 <= year <= 49  :
                                    print ("Registration fee : 6,000")
                            elif 50 <= year <= 55 :
                                    print ("Registration fee : 7,000")
                            else : 
                                    print ("Registration fee : 7,750")
                        else : print ("Invalid semester")
                    else :
                        sem = int(input("Enter semester : "))
                        if sem == 1 or sem == 2 :
                            if 48 <= year <= 49  :
                                    print ("Registration fee : 12,000")
                            elif 50 <= year <= 55 :
                                    print ("Registration fee : 4,500")
                            else : 
                                    print ("Registration fee : 17,000")
                        elif sem == 3 :
                            if 48 <= year <= 49  :
                                    print ("Registration fee : 4,000")
                            elif 50 <= year <= 55 :
                                    print ("Registration fee : 4,500")
                            else : 
                                    print ("Registration fee : 5,250")
                        else : print ("Invalid semester")
            else : print ("Invalid ID")
        else : print ("Invalid ID")
    else : print ("Invalid ID")
