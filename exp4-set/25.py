# Friends of two users
user1 = {"Amit", "Rahul", "Sneha", "Priya"}
user2 = {"Rahul", "Priya", "Karan", "Neha"}

# Mutual friends
mutual = user1 & user2

# Friends unique to User 1
unique_user1 = user1 - user2

# Friends unique to User 2
unique_user2 = user2 - user1

# Total unique friends
total_unique = user1 | user2

print("Mutual friends:", mutual)
print("Friends unique to User 1:", unique_user1)
print("Friends unique to User 2:", unique_user2)
print("Total unique friends:", total_unique)
print("Number of unique friends:", len(total_unique))
