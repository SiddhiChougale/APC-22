def add_book():
    f = open("books.txt", "a")

    book_id = input("Enter book ID: ")
    title = input("Enter title: ")
    author = input("Enter author: ")

    f.write(book_id + "," + title + "," + author + ",Available\n")
    f.close()

    print("Book added.")


def search_book():
    f = open("books.txt", "r")

    book_id = input("Enter book ID: ")

    for line in f:
        data = line.strip().split(",")

        if data[0] == book_id:
            print("Book found:", data)
            break
    else:
        print("Book not found.")

    f.close()


def issue_book():
    f = open("books.txt", "r")
    lines = f.readlines()
    f.close()

    book_id = input("Enter book ID: ")

    f = open("books.txt", "w")

    for line in lines:
        data = line.strip().split(",")

        if data[0] == book_id:
            if data[3] == "Available":
                data[3] = "Issued"
                print("Book issued.")
            else:
                print("Book is already issued.")

            line = ",".join(data) + "\n"

        f.write(line)

    f.close()


def return_book():
    f = open("books.txt", "r")
    lines = f.readlines()
    f.close()

    book_id = input("Enter book ID: ")

    f = open("books.txt", "w")

    for line in lines:
        data = line.strip().split(",")

        if data[0] == book_id:
            data[3] = "Available"
            line = ",".join(data) + "\n"
            print("Book returned.")

        f.write(line)

    f.close()


def display_available():
    f = open("books.txt", "r")

    print("Available Books:")

    for line in f:
        data = line.strip().split(",")

        if data[3] == "Available":
            print(data)

    f.close()


add_book()
search_book()
issue_book()
return_book()
display_available()
