word = input("Next word : ").strip()
s = ''
while word != '.' :
    s += ' ' + word
    word = input("Next word : ").strip()
print ("Sentence:"+s)
