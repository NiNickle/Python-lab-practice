#Lab2_4
#Nichaphat Chawananukul 6234422823

a,b,c=input("Length of 3 sides: ").split(", ")
a=float(a)
b=float(b)
c=float(c)
TF=str(a<b+c and b<a+c and c<a+b)
print ("Triangle: "+TF)