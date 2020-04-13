cnt,stock=0,{}
size_dict={'S':1,'M':2,'L':3,'XL':4,1:'S',2:'M',3:'L',4:'XL'}
while cnt<10:
    product_ID,size,num=input( 'Enter product ID, size, number of items : ').split()
    num=int(num)
    product_ID=int(product_ID)
    size=size.upper()
    if (product_ID,size) in stock :
        num_update=stock[(product_ID,size)]+num
        stock.update({(product_ID,size):num_update})
    else:
        stock.update({(product_ID,size):num})
    cnt+=1
stock_lst=[(i,size_dict[j],stock[(i,j)]) for i,j in stock.keys()]    
stock_lst.sort()
print("\nStock:")
for k in range(len(stock_lst)):
    print(stock_lst[k][0],size_dict[stock_lst[k][1]],stock_lst[k][2])
















