word = input("Next word : ").strip()
s = ''
while word != '.' :
    s = s + ' ' + word
    word = input("Next word : ").strip()
print ("Sentence:"+s)