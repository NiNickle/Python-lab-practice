text=input(":")
cnt=0
i=0
if len(text)<9 :
    print(cnt,"IDs")
else:
    while i<len(text):
        if text[i]=="6" and text[i+1]=="2":
            if text[i+8]=="2" and text[i+9]=="3":
                cnt+=1
                i+=10
                continue
            else :
                i+=1
        else :
            i+=1
    print(cnt,"IDs")
            