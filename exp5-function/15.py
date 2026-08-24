def unique_elements(numbers):
    new_list = []

    for n in numbers:
        if n not in new_list:
            new_list.append(n)

    return new_list

numbers = [10, 20, 10, 30, 20, 40]

print("Unique elements =", unique_elements(numbers))
