# #reading
# with open('file.txt','r') as file:
#     content=file.read()
#     print(content)

# r = Read
f = open("file.txt", "r")
print(f.read())
f.close()

# w = Write
f = open("file.txt", "w")
f.write("Hello")
f.close()

# a = Append
f = open("file.txt", "a")
f.write("\nWelcome")
f.close()
