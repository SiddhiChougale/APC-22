def power(base, exponent):
    result = 1

    for i in range(exponent):
        result = result * base

    return result

base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))

print("Answer =", power(base, exponent))
