n = int(input("Number of students : "))
cnt       = 1
total     = 0
HighScore = 0
PassTotal = 0
PassStu   = 0
FailTotal = 0
FailStu   = 0 
while cnt <= n :
    score = float(input("Student "+str(cnt)+" : "))
    cnt+=1
    total = total + score
    if score >= HighScore : 
        HighScore = score
    if score >= 5 :
        PassTotal = PassTotal + score
        PassStu += 1 
    else :
        FailTotal = FailTotal + score
        FailStu += 1
if PassStu == 0 : PassStu += 1
if FailStu == 0 : FailStu += 1
AvgScore = total / n
PassAvg = PassTotal / PassStu
FailAvg = FailTotal / FailStu
print ("Average score :",AvgScore)
print ("Average passing score :",PassAvg)
print ("Average failing score :",FailAvg)
print ("Highest score :",HighScore)


