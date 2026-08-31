f=open("student.txt","r")

text=f.read()
words=text.split()
# count=0
# for word in f:
#     count+=1
print("Total words: ",len(words))
f.close()
