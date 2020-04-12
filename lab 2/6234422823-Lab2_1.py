#Lab2_1
#Nichaphat Chawananukul 6234422823

import math as m
a,b,c=input("Enter coefficients a, b, c : ").split(", ")
a=float(a)
b=float(b)
c=float(c)
x1=(-b+m.sqrt(b**2-4*a*c))/(2*a)
x2=(-b-m.sqrt(b**2-4*a*c))/(2*a)
print ("x = "+str(x1)+", "+str(x2))