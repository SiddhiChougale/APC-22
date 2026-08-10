numbers = []

for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)

total = sum(numbers)
average = total / 10

print("Sum =", total)
print("Average =", average)