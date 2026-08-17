# Available books
available_books = {"Python", "Java", "C++", "HTML", "SQL"}

# Requested books
requested_books = {"Python", "SQL", "JavaScript", "C"}

# Find requested books that are available
available_requested = requested_books & available_books

print("Requested books that are available:", available_requested)
