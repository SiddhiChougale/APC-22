from array import array

arr = array('i', [10, 20, 30])

print( arr)

arr.frombytes()

print("After byteswap:", arr)
