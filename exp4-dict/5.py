cities = {
    "Pune": 7000000,
    "Mumbai": 20000000,
    "Delhi": 30000000,
    "Chennai": 7000000
}

city = input("Enter city to remove: ")

cities.pop(city, None)

print(cities)
