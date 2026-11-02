import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Student Form")
root.geometry("350x400")

# Roll Number
tk.Label(root, text="Roll Number:").pack(pady=5)
roll_entry = tk.Entry(root)
roll_entry.pack()

# Name
tk.Label(root, text="Name:").pack(pady=5)
name_entry = tk.Entry(root)
name_entry.pack()

# Subjects
tk.Label(root, text="Select Subjects:").pack(pady=10)

python_var = tk.IntVar()
java_var = tk.IntVar()
dbms_var = tk.IntVar()

tk.Checkbutton(root, text="Python",
               variable=python_var).pack()

tk.Checkbutton(root, text="Java",
               variable=java_var).pack()

tk.Checkbutton(root, text="DBMS",
               variable=dbms_var).pack()


# Submit function
def submit():
    roll = roll_entry.get().strip()
    name = name_entry.get().strip()

    subjects = []

    if python_var.get():
        subjects.append("Python")
    if java_var.get():
        subjects.append("Java")
    if dbms_var.get():
        subjects.append("DBMS")

    # Validation
    if roll == "" or not roll.isdigit():
        messagebox.showerror(
            "Error", "Enter a valid numeric roll number!"
        )
        return

    if name == "" or not name.replace(" ", "").isalpha():
        messagebox.showerror(
            "Error", "Enter a valid name!"
        )
        return

    if len(subjects) == 0:
        messagebox.showerror(
            "Error", "Select at least one subject!"
        )
        return

    messagebox.showinfo(
        "Success",
        f"Student Details\n\n"
        f"Roll Number: {roll}\n"
        f"Name: {name}\n"
        f"Subjects: {', '.join(subjects)}"
    )


# Submit button
tk.Button(root, text="Submit",
          command=submit,
          bg="green", fg="white").pack(pady=20)

root.mainloop()