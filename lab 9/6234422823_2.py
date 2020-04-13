with open('exam.txt') as f1 :
    examAns=[ans.strip().split() for ans in f1.readlines()]
with open('sol.txt') as f2 :
    examKey=f2.readline().strip().split()
scoresList,score=[],0
validCnt=[0 for x in range(len(examKey))]
for item in examAns :
    for i in range(len(item)):
        if item[i]==examKey[i]:
            score+=1
            validCnt[i]+=1
    scoresList.append(score)
    score=0
print("Student score:\n"+str(scoresList)+"\n")
for n in range(len(examKey)):
    print("Question",n+1,":",validCnt[n]/len(examAns))
    if min(validCnt)==validCnt[n]:
        easyQ=n+1
    if max(validCnt)==validCnt[n]:
        hardQ=n+1
print("\n"+str(easyQ)+" is the hardest question.\n"+str(hardQ)+" is the easiest question.")
