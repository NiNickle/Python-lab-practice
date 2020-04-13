name = input("Enter username : ").strip()
cnt = 0
while name != "Nichaphat" and cnt < 2 :
    name = input("Incorrect. Enter again : ").strip()
    cnt+=1
if name == "Nichaphat" :
    print ("Hello,",name)
else :
    print ("Not allow. Incorrect name.")