f=open("book.txt")
line=[x.split() for x in f.readlines()]
word_all=[]
cont,cnt,x=[],1,1
for i in range (len(line)):
    word=[x.strip("?,.:;()– ").lower() for x in line[i]]
    word_all+=word
word_all.sort()
for i in range (len(word_all)):
    cnt=1
    if i<(len(word_all)):
        for j in range (1,len(word_all)):
            if j<(len(word_all)) and i<j:
                if word_all[i]==word_all[j] and i!=j:
                    cnt+=1
                    del word_all[j]
                    j=i+1
        cont+=[cnt]
print("In Alphabetical order:") 
for i in range (len(cont)):
    while x!=0:
        if len(word_all[i])<8:
            word_all[i]+=" "
        else:
            break
    print(word_all[i],cont[i])
print("By frequency:")
word_dict={i:{word_all[i]:cont[i]} for i in range (len(word_all)) for j in range (len(cont))}
word_re_all=[]
re,Max=0,[]
Max_minus=max(cont)
for i in cont:
    if i == max(cont):
        re+=1
        Max+=[re]
    else:
        re+=1
re=0
Max.sort(reverse=True)
for i in range (len(Max)):
    print(cont[Max[i]-1],"\t",word_all[Max[i]-1])
while Max_minus-1!=min(cont):    
    Mean=[]
    for i in cont:
        if i == min(cont):
            re+=1
            Mean+=[re]
        else:
            re+=1
        re=0
        Mean.sort(reverse=True)
        for i in range (len(Mean)):
            print(cont[Mean[i]-1],"\t",word_all[Mean[i]-1])
    Max_minus-=1
Min=[]
for i in cont:
    if i == min(cont):
        re+=1
        Min+=[re]
    else:
        re+=1
re=0
Min.sort(reverse=True)
for i in range (len(Min)):
    print(cont[Min[i]-1],"\t",word_all[Min[i]-1])
f.close()