with open('score.txt') as f:
    lst=[i.strip().split() for i in f.readlines()]
score_list=[[int(lst[j][1]),lst[j][0]] for j in range(len(lst))]
score_list.sort(reverse=True)
for k in range(len(score_list)):
    print(score_list[k][1])