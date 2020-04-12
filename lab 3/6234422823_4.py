w,wUnit=input("Weight : ").split()
h,hUnit=input("Height : ").split()
w=float(w)
h=float(h)

if wUnit=="lbs" : w=w*0.45359237
if hUnit=="ft" : h=h*0.3048
if hUnit=="cm" : h=h*0.01

bmi=w/h**2

if   bmi<18.5 : print("ผอม")
elif 18.5<=bmi<23.0 : print("รูปร่างปกติ")
elif 23.0<=bmi<25.0 : print("รูปร่างอ้วน")
elif 25.0<=bmi<30.0 : print("อ้วนระดับ 1")
else : print("อ้วนระดับ 2")