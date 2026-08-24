def second_largest(numbers):
    unique = list(set(numbers))
    unique.sort()

    return unique[-2]

numbers = [10, 30, 20, 50, 40]

print("Second largest =", second_largest(numbers))
