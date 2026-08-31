f = open("tr.txt", "r")

total_deposits = 0
total_withdrawals = 0
balance = 0
largest = 0

for line in f:
    amount = int(line.strip())

    if amount > 0:
        total_deposits = total_deposits + amount
    else:
        total_withdrawals = total_withdrawals + abs(amount)

    balance = balance + amount

    if abs(amount) > largest:
        largest = abs(amount)

f.close()

print("Total deposits:", total_deposits)
print("Total withdrawals:", total_withdrawals)
print("Final balance:", balance)
print("Largest transaction:", largest)
