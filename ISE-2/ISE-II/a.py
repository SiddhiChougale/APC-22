file=open("Student.txt","w")
file.write("13:Prachi\n")
file.write("17:Shruti\n")
file.write("22:Siddhi\n")
file.write("53:Kalyani\n")
file.write("53:Vaishnavi\n")
file.close()
print("Student.txt file created")
rn=input("Enter roll number:")
with open("students.txt", "r") as file:
    found = False
    for line in file:
            data = line.strip().split(",")
    
            if data[0] == rn:
                print("Student Found")
                print("Roll No:", data[0])
                print("Name:", data[1])
                print("Marks:", data[2])
                found = True
                break
    
    if not found:
        print("Student not found")
     