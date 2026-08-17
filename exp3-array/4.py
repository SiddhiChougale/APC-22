from array import array

numbers = array('i', [10, 20, 30, 40, 50])

search = int(input("Enter number to search: "))

if search in numbers:
    print("Element found")
else:
    print("Element not found")
