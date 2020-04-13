text=input("Enter some text : ")
cnt=0
i=0
while i<len(text):
    if text[i]=="(":
        n=text.find(")",i+1,len(text))
        if n>0 :
            cnt+=1
            i=n+1
            #continue
        else :
            i+=1
    else:
        i+=1
print("There are",cnt,"pairs of () .")