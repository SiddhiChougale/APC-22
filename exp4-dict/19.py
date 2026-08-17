data = {
    "A": 10,
    "B": 20,
    "C": 10,
    "D": 30,
    "E": 20
}

result = {}

for key, value in data.items():
    if value not in result.values():
        result[key] = value

print("Dictionary without duplicate values:", result)
