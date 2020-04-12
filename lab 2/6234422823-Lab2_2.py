#Lab2_2
#Nichaphat Chawananukul 6234422823

a,b,c=input("Enter coefficients a, b, c : ").split(", ")
a=float(a)
b=float(b)
c=float(c)
ans=b**2-4*a*c
TF=str(ans>=0 and a!=0)
print("Can use quadratic formula: "+TF)