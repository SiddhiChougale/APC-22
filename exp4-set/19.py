# Students present in each session
morning = {"Amit", "Rahul", "Sneha", "Priya"}
afternoon = {"Rahul", "Priya", "Karan", "Neha"}

# Students present in both sessions
both = morning & afternoon

# Students present only in the morning
morning_only = morning - afternoon

# Students present only in the afternoon
afternoon_only = afternoon - morning

# Students present in at least one session
at_least_one = morning | afternoon

print("Both sessions:", both)
print("Only morning:", morning_only)
print("Only afternoon:", afternoon_only)
print("At least one session:", at_least_one)
