f = open("10.py", "r")

lines = f.readlines()

f.close()

f = open("newprogram.py", "w")

for line in lines:
    if "#" not in line:
        f.write(line)

f.close()

print("Comments removed successfully.")
