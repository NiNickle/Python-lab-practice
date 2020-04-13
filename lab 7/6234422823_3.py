text=input("Enter some text : ")
cnt=0
i=0
if len(text)<10:
    print("There are",cnt,"student IDs .")
else :
    while i<len(text):
        if len(text)-i<9 :
            break
        elif text[i]=="6" and text[i+1]=="2":
            if text[i+8]=="2" and text[i+9]=="3":
                cnt+=1
                i+=10
            else:
                i+=1
        else :
            i+=1
    print("There are",cnt,"student IDs .")

