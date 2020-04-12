import math as m
a,b,c=input("Enter coefficients a, b, c : ").split(", ")
a=float(a)
b=float(b)
c=float(c)

ans=b**2-4*a*c

if a==0 or ans<0 :
    print("No real solution")
else :
    x1=(-b+m.sqrt(b**2-4*a*c))/(2*a)
    x2=(-b-m.sqrt(b**2-4*a*c))/(2*a)
    print("x = "+str(x1)+", "+str(x2))
