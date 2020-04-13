x,y=[int(i) for i in input("Initial position : ").split(",")]
isMove = True
f=open('move.txt','r')
commands=[command.strip() for command in f.readlines()]
for line in commands :
    if line=="R" :
        if x<9:
            x=x+1
    elif line=="L":
        if x>-9:
            x=x-1
    elif line=="U":
        if y<9:
            y=y+1
    elif line=="D":
        if y>-9:
            y=y-1
    else :
        isMove = False
        break
if not isMove :
    print("Invalid command")
else :
    print("Robot stops at",x,",",y)
f.close()