# -------------------------- Problem 1 ---------------------------------------
with open('score.txt', 'r') as f:
    studentList = f.readlines()
scList = []                         # เป็นลิสต์ของลิสต์ของคะแนนกับชื่อ
for line in studentList:
    name, score = line.strip().split()
    score = float(score)
    scList.append([score, name])
scList.sort(reverse=True)           # เรียงด้วยคะแนนก่อน แล้วเรียงด้วยชื่อ
for sc_name in scList:
    print(sc_name[1])               # ดึงชื่อมาพิมพ์
    
# ------------------------- Problem 2 ------------------------------------
monthlyIncome = []                  # เก็บรายได้ต่อเดือน
print('Enter monthly income in 2561:')
for i in range(12):
    inc = int(input())  
    monthlyIncome.append(inc)
quarterlyIncome = []                # เก็บรายได้ต่อไตรมาส
for i in range(0,12,3):
    threeMonthIncome = monthlyIncome[i:i+3]
    quarterlyIncome.append(sum(threeMonthIncome))
highQtIncome = max(quarterlyIncome) # หารายได้สูงสุดของไตรมาส
for i in range(4):                  # หาไตรมาสของรายได้สูงสุด
    if quarterlyIncome[i]==highQtIncome:
        print('Highest income is in quarter',i+1)

# ----------------------- Problem 3 -----------------------------------
stock = {}			         # ดิคชันนารีที่มี product ID, เลข size เป็นคีย์ คู่กับค่าที่เป็นจำนวนสินค้
sizeTable = {'S':0, 'M':1, 'L': 2, 'XL':3}  # เก็บเลข size 
revSz = ['S', 'M', 'L', 'XL']                  # ใช้แปลงเลข size กลับมาเป็น S, M, L, XL
for i in range(10):
    product, size, num = input('Enter product ID, size, number of items: ').split()
    num = int(num)
    k = (product, sizeTable[size])       # สร้างคีย์จาก product ID และ size ที่แปลงเป็นตัวเลขแล้ว
    if k in stock.keys():                     # เช็คว่ามีคีย์นี้ในดิคชันนารีหรือยัง
        stock[k] = stock[k]+num 
    else:
        stock[k] = num
sortK = list(stock.keys())	         # ดึงคีย์มาสร้างเป็นลิสต์
sortK.sort()		         # เรียงคีย์
for product, sCode in sortK:
    print(product, revSz[sCode],stock[product, sCode])  # แปลงเลข size เป็น S, M, L, XL ด้วย revSz
          