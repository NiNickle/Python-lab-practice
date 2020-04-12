import math
choice=input("Choose circle, square or rectangle : ")

if choice=="circle" :
    r=float(input("Length of the radius of the circle : "))
    area=math.pi*r**2
    print("Area is",area)

elif choice=="square" :
    s=float(input("Length of the side of the square : "))
    area=s**2
    print("Area is",area)

elif choice=="rectangle" :
    s1,s2=input("Length of two side of the square : ").split(", ")
    s1=float(s1)
    s2=float(s2)
    area=s1*s2
    print("Area is",area)

else : print("Invalid choice.")