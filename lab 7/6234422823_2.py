text=input("Enter your message : ")
cipherText=''
decodeText='''ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz1234567890,.?!'''
encodeText=''',.?!MNOPQRSTUVWXYZABCDEFGHIJKLlmnopqrstuvwxyzabcdefghijk 1234567890'''

for i in range(len(text)) :
    n=decodeText.find(text[i])
    cipherText=cipherText+encodeText[n]
print("cipher text:\t     "+cipherText)

