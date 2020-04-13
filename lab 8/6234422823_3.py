f=open('score.txt','r')
Score=[int(item.strip()) for item in f.readlines()]

avgScore = sum(Score)/len(Score)
print("Average score =",avgScore)

maxScore = max(Score)
print("Max score =",maxScore)

minScore = min(Score)
print("Min score =",minScore)

Score.sort()
maxNo=Score.count(maxScore)
print("Frequencies:")
cnt=1
for i in range (len(Score)) :
    if Score[i]==maxScore:
        print(maxNo,"of",Score[i])
        break
    if Score[i]==Score[i+1] and i-1<len(Score):
        cnt+=1
    else:
        print(cnt,"of",Score[i])
        cnt=1
f.close()


