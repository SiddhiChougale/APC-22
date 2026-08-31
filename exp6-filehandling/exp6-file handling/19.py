f = open("att.txt", "r")

for line in f:
    data = line.strip().split(",")

    name = data[0]
    present = int(data[1])
    total = int(data[2])

    percentage = (present / total) * 100

    print(name, "Attendance:", percentage, "%")

    if percentage < 75:
        print(name, "has attendance below 75%")

f.close()
