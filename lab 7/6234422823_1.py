text=input("Enter text : ")
newText=''
for i in range(len(text)) :
    if text[i] not in '''/.-?!"'(){}!,;'''+'\t' :
        newText=newText+text[i]
print("--"+newText+"--")