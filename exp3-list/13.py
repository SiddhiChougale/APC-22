numbers = []

for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)

numbers.sort()

print("Ascending order:", numbers)

numbers.reverse()

print("Descending order:", numbers)