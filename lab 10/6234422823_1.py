#facGroup={faculty:group_number}
facGroup={21:1,22:2,23:1,24:2,25:1,26:2,27:2,28:1,29:2,30:1,31:1,32:1,33:1,34:2,35:1,36:1,37:1,38:1,39:1,51:2,53:1}
idNum=input("Enter student ID : ").strip()
if len(idNum) != 10 :
    print ("Invalid ID")
else :
    fac=int(idNum[-2:])
    year=int(idNum[0:2])
    if 48<=year :
        if int(idNum[2]) in [3,4,7] :
            if fac in facGroup:
                sem = int(input("Enter semester : "))
                if int(idNum[2]) == 7 :
                    study_prog="master"
                else :
                    study_prog="bachelor"
                if 48<=year<=49:
                    if  sem==1 or sem==2 or sem==3:
                        #tuition_fee={(faculty group number,study program,semester):tuition fee}
                        tuition_fee={(1,"bachelor",1):"16,000",(1,"bachelor",2):"bachelor",(1,"bachelor",3):"4,000",(1,"master",1):"22,500",(1,"master",2):"22,500",(1,"master",3):"6,000", \
                                    (2,"bachelor",1):"12,000",(2,"bachelor",2):"12,000",(2,"bachelor",3):"4,000",(2,"master",1):"16,500",(2,"master",2):"16,500",(2,"master",3):"6,000"}
                        print("Registration fee :",tuition_fee[(facGroup[fac],study_prog,sem)])
                    else:print ("Invalid semester")
                if 50<=year<=55:
                    if  sem==1 or sem==2 or sem==3:
                        #tuition_fee={(faculty group number,study program,semester):tuition fee}
                        tuition_fee={(1,"bachelor",1):"18,000",(1,"bachelor",2):"18,000",(1,"bachelor",3):"4,500",(1,"master",1):"26,000",(1,"master",2):"26,000",(1,"master",3):"7,000", \
                                    (2,"bachelor",1):"14,500",(2,"bachelor",2):"14,500",(2,"bachelor",3):"4,500",(2,"master",1):"19,000",(2,"master",2):"19,000",(2,"master",3):"7,000"}
                        print("Registration fee :",tuition_fee[(facGroup[fac],study_prog,sem)])
                    else:print ("Invalid semester")
                if 56<=year:
                    if  sem==1 or sem==2 or sem==3:
                        #tuition_fee={(faculty group number,study program,semester):tuition fee}
                        tuition_fee={(1,"bachelor",1):"21,000",(1,"bachelor",2):"21,000",(1,"bachelor",3):"5,250",(1,"master",1):"31,000",(1,"master",2):"31,000",(1,"master",3):"7,750", \
                                    (2,"bachelor",1):"17,000",(2,"bachelor",2):"17,000",(2,"bachelor",3):"5,250",(2,"master",1):"23,000",(2,"master",2):"23,000",(2,"master",3):"7,750"}
                        print("Registration fee :",tuition_fee[(facGroup[fac],study_prog,sem)])
                    else:print ("Invalid semester")
            else: print ("Invalid ID")
        else: print ("Invalid ID")
    else: print ("Invalid ID")

