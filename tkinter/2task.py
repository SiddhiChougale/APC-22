from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import re

root = Tk()
root.title("Registration Form")
root.geometry("400x500")

# Name
Label(root, text="Enter Full Name").pack(pady=5)
name = Entry(root, width=30)
name.pack()

# Mobile Number
Label(root, text="Mobile Number").pack(pady=5)
mobile_frame = Frame(root)
mobile_frame.pack()

Label(mobile_frame, text="+91").pack(side=LEFT)
mobile = Entry(mobile_frame, width=25)
mobile.pack(side=LEFT)

# State
Label(root, text="State").pack(pady=5)
state = ttk.Combobox(root, values=["Maharashtra", "Goa", "Karnataka"])
state.pack()

# District
Label(root, text="District").pack(pady=5)
district = ttk.Combobox(root, values=["Kolhapur", "Pune", "Mumbai"])
district.pack()

# Taluka
Label(root, text="Taluka").pack(pady=5)
taluka = ttk.Combobox(root, values=["Karvir", "Hatkanangale", "Panhala"])
taluka.pack()

# Address
Label(root, text="Address").pack(pady=5)
address = Entry(root, width=30)
address.pack()


# Validation
def submit():
    n = name.get().strip()
    m = mobile.get().strip()
    s = state.get()
    d = district.get()
    t = taluka.get()
    a = address.get().strip()

    if not re.fullmatch(r"[A-Za-z ]+", n) or len(n.split()) < 2:
        messagebox.showerror("Error", "Enter your full name.")
    elif not re.fullmatch(r"[6-9][0-9]{9}", m):
        messagebox.showerror("Error", "Enter a valid 10-digit mobile number.")
    elif s == "" or d == "" or t == "":
        messagebox.showerror("Error", "Select State, District and Taluka.")
    elif a == "":
        messagebox.showerror("Error", "Enter your address.")
    else:
        messagebox.showinfo("Success", "Registration Successful!")


# Submit Button
Button(root, text="Submit", command=submit).pack(pady=20)

root.mainloop()