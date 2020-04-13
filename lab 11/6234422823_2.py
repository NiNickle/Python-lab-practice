print("Enter monthly income in 2561:")
month,income_list=0,[]
while month<12 :
    income=input()
    income_list.append(int(income))
    month+=1
quater=[sum(income_list[i:i+3]) for i in range(0,12,3)]
for j in range(4) :
    if quater[j]==max(quater) : 
        print("Highest income in the quarter",j+1)