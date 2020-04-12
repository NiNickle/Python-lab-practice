#Lab2_5
#Nichaphat Chawananukul 6234422823

a,b,c=input("Length of 3 sides: ").split(", ")
a=float(a)
b=float(b)
c=float(c)
TF=str(a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==a**2+b**2)
print ("Right triangle: "+TF)
