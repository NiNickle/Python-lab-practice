w=float(input("Weight (kg.) : "))
h=float(input("Height (m.) : "))

bmi=w/h**2
   
if   bmi<18.5 : print("ผอม")
elif 18.5<=bmi<23.0 : print("รูปร่างปกติ")
elif 23.0<=bmi<25.0 : print("รูปร่างอ้วน")
elif 25.0<=bmi<30.0 : print("อ้วนระดับ 1")
else : print("อ้วนระดับ 2")
