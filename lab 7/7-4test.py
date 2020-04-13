text=input("Enter some text : ")
cnt=0
i=0
while i<len(text):
    if text[i]=="(":
        n=text.find(")",i+1,len(text)-1)
        if n>0 :
            cnt+=1
            i=n+1
            continue
        else :
            i+=1
    else:
        i+=1
print(cnt,"pairs of ()")
        
'''
for i in range(len(text)):
    if text[i]=="(":
        n= text.find(")")

for i in range(len(text)):
    if text[i]=="(":
        for j in range(len(text)):
            if text[j]==")":
                cnt=cnt+1
                text=text.replace(text[j],"x",2)
print("There are",cnt,"pairs of () .")
'''