num=[]

for i in range(15):
    list=int(input("enter the numbers:"))
    num.append(list)

even=0
odd=0
for list in num:
    if list%2==0:
        even+=1
    else:
        odd+=1

print("Even no.: ",even)
print("Odd no.: ,",odd)