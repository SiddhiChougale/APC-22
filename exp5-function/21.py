def total_bill(prices, quantities):
    total = 0

    for i in range(len(prices)):
        total = total + prices[i] * quantities[i]

    discount = total * 10 / 100
    final_bill = total - discount

    return final_bill

prices = [100, 200, 50]
quantities = [2, 1, 3]

print("Total bill after discount =", total_bill(prices, quantities))
