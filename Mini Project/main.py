
import tkinter as tk
from tkinter import ttk, messagebox

from database import get_menu_items, save_order
from billing import (
    add_item,
    generate_bill,
    calculate_subtotal,
    calculate_gst
)


# ---------------- COLORS ----------------

BG = "#F8F5EC"
NAVY = "#17365D"
LIGHT_BLUE = "#DCEAF8"
BLUE = "#245A8D"
GREEN = "#218838"
WHITE = "#FFFFFF"
TEXT = "#243447"

orders = []


# ---------------- FUNCTIONS ----------------

def add_to_order():
    selected = menu_table.selection()

    if not selected:
        messagebox.showwarning("Warning", "Please select a food item.")
        return

    try:
        quantity = int(quantity_box.get())

        if quantity <= 0:
            messagebox.showwarning(
                "Invalid Quantity",
                "Quantity must be greater than 0."
            )
            return

    except ValueError:
        messagebox.showwarning(
            "Invalid Quantity",
            "Enter a valid quantity."
        )
        return

    item_id = int(selected[0])

    if item_id not in menu_data:
        messagebox.showwarning(
            "Invalid Selection",
            "Please select a food item, not a category."
        )
        return

    category, name, price = menu_data[item_id]

    add_item(orders, name, price, quantity)

    row_tag = "even" if len(orders) % 2 == 0 else "odd"

    order_table.insert(
        "",
        "end",
        values=(name, price, quantity, price * quantity),
        tags=(row_tag,)
    )

    update_total()


def update_total():
    subtotal = 0

    for order in orders:
        subtotal += order[3]

    total_label.config(
        text="Subtotal: Rs. " + format(subtotal, ".2f")
    )


def show_bill():
    if not orders:
        messagebox.showwarning(
            "Empty Order",
            "Please add food items first."
        )
        return

    try:
        subtotal = calculate_subtotal(orders)
        gst = calculate_gst(subtotal)
        grand_total = subtotal + gst

        # Save bill and items in MySQL
        order_id = save_order(
            orders, subtotal, gst, grand_total
        )

        bill_text = generate_bill(orders)

        bill_text = (
            "Order ID: " + str(order_id) + "\n\n" + bill_text
        )

        # Bill window
        bill_window = tk.Toplevel(root)
        bill_window.title("Cafe Bill")
        bill_window.geometry("650x450")
        bill_window.configure(bg=BG)

        tk.Label(
            bill_window,
            text="CAFE BILL",
            font=("Arial", 18, "bold"),
            bg=BG,
            fg=NAVY,
            pady=10
        ).pack()

        bill_area = tk.Text(
            bill_window,
            font=("Courier New", 11),
            wrap="none",
            bg=WHITE,
            fg=TEXT,
            padx=15,
            pady=15,
            relief="solid",
            borderwidth=1
        )

        bill_area.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=10
        )

        bill_area.insert("1.0", bill_text)
        bill_area.config(state="disabled")

    except Exception as error:
        messagebox.showerror(
            "Database Error",
            "Could not save the bill.\n\n" + str(error)
        )


def clear_order():
    orders.clear()

    for row in order_table.get_children():
        order_table.delete(row)

    update_total()


# ---------------- MAIN WINDOW ----------------

root = tk.Tk()
root.title("Cafe Billing System")
root.geometry("1100x700")
root.minsize(900, 600)
root.configure(bg=BG)


# ---------------- TABLE STYLING ----------------

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Cafe.Treeview",
    background=WHITE,
    foreground=TEXT,
    fieldbackground=WHITE,
    rowheight=30,
    font=("Arial", 10)
)

style.configure(
    "Cafe.Treeview.Heading",
    background=LIGHT_BLUE,
    foreground=NAVY,
    font=("Arial", 10, "bold"),
    relief="flat",
    padding=8
)

style.map(
    "Cafe.Treeview",
    background=[("selected", BLUE)],
    foreground=[("selected", WHITE)]
)

style.map(
    "Cafe.Treeview.Heading",
    background=[("active", "#C5DDF5")]
)


# ---------------- TITLE SECTION ----------------

title = tk.Label(
    root,
    text="CAFE BILLING SYSTEM",
    font=("Arial", 25, "bold"),
    bg=BG,
    fg=NAVY,
    pady=10
)
title.pack()

subtitle = tk.Label(
    root,
    text="Good Food  •  Good Mood",
    font=("Arial", 11, "italic"),
    bg=BG,
    fg=BLUE
)
subtitle.pack(pady=(0, 10))


# ---------------- MAIN TWO-PART LAYOUT ----------------

main_frame = tk.Frame(root, bg=BG)
main_frame.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=8
)

# LEFT SIDE - YOUR ORDER

left_frame = tk.Frame(
    main_frame,
    bg=BG
)

left_frame.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(0, 8)
)


# RIGHT SIDE - CAFE MENU

right_frame = tk.Frame(
    main_frame,
    bg=BG
)

right_frame.pack(
    side="right",
    fill="both",
    expand=True,
    padx=(5, 0)
)


# ==================================================
# LEFT SIDE - YOUR ORDER
# ==================================================

order_frame = tk.LabelFrame(
    left_frame,
    text="  Your Order  ",
    font=("Arial", 14, "bold"),
    bg=BG,
    fg=NAVY,
    bd=2,
    relief="groove"
)

order_frame.pack(
    fill="both",
    expand=True,
    pady=5
)


order_table = ttk.Treeview(
    order_frame,
    columns=("Food", "Price", "Quantity", "Total"),
    show="headings",
    height=8,
    style="Cafe.Treeview"
)

order_table.heading("Food", text="Food Item")
order_table.heading("Price", text="Price")
order_table.heading("Quantity", text="Qty")
order_table.heading("Total", text="Total")

order_table.column("Food", width=145)
order_table.column("Price", width=75, anchor="center")
order_table.column("Quantity", width=55, anchor="center")
order_table.column("Total", width=85, anchor="center")

order_table.tag_configure(
    "odd",
    background=WHITE
)

order_table.tag_configure(
    "even",
    background="#EDF4FB"
)

order_table.pack(
    fill="both",
    expand=True,
    padx=5,
    pady=8
)


# SUBTOTAL

total_label = tk.Label(
    left_frame,
    text="Subtotal: Rs. 0.00",
    font=("Arial", 15, "bold"),
    bg=LIGHT_BLUE,
    fg=NAVY,
    padx=8,
    pady=12,
    relief="solid",
    bd=1
)

total_label.pack(
    fill="x",
    pady=10
)


# ACTION BUTTONS

button_frame = tk.Frame(
    left_frame,
    bg=BG
)

button_frame.pack(
    fill="x",
    pady=8
)


generate_bill_button = tk.Button(
    button_frame,
    text="Generate Bill",
    command=show_bill,
    font=("Arial", 11, "bold"),
    bg=GREEN,
    fg=WHITE,
    activebackground="#176B2C",
    activeforeground=WHITE,
    width=14,
    pady=9,
    relief="flat",
    cursor="hand2"
)

generate_bill_button.pack(
    fill="x",
    pady=5
)


new_order_button = tk.Button(
    button_frame,
    text="New Order",
    command=clear_order,
    font=("Arial", 11, "bold"),
    bg=LIGHT_BLUE,
    fg=NAVY,
    activebackground="#C5DDF5",
    activeforeground=NAVY,
    width=14,
    pady=9,
    relief="solid",
    bd=1,
    cursor="hand2"
)

new_order_button.pack(
    fill="x",
    pady=5
)


# ==================================================
# RIGHT SIDE - CAFE MENU
# ==================================================

menu_frame = tk.LabelFrame(
    right_frame,
    text="  Cafe Menu  ",
    font=("Arial", 14, "bold"),
    bg=BG,
    fg=NAVY,
    bd=2,
    relief="groove"
)

menu_frame.pack(
    fill="both",
    expand=True,
    pady=5
)


menu_table = ttk.Treeview(
    menu_frame,
    columns=("Food", "Price"),
    show="tree headings",
    height=6,
    style="Cafe.Treeview"
)

menu_table.heading("#0", text="Category")
menu_table.heading("Food", text="Food Item")
menu_table.heading("Price", text="Price")

menu_table.column("#0", width=105)
menu_table.column("Food", width=145)
menu_table.column("Price", width=75, anchor="center")


menu_table.tag_configure(
    "category",
    background=LIGHT_BLUE,
    foreground=NAVY,
    font=("Arial", 10, "bold")
)


# LOAD MENU ITEMS FROM MYSQL

items = get_menu_items()

menu_data = {}

for item in items:
    item_id, category, name, price = item
    menu_data[item_id] = (category, name, float(price))


# DISPLAY MENU CATEGORY-WISE

categories = ["Pizza", "Sandwich", "Beverages"]

for category in categories:

    category_id = menu_table.insert(
        "",
        "end",
        text=category,
        open=True,
        tags=("category",)
    )

    for item in items:

        item_id, item_category, name, price = item

        if item_category == category:

            menu_table.insert(
                category_id,
                "end",
                iid=str(item_id),
                values=(name, price)
            )


menu_table.pack(
    fill="both",
    expand=True,
    padx=8,
    pady=10
)


# ---------------- QUANTITY SECTION ----------------

quantity_frame = tk.LabelFrame(
    right_frame,
    text="Select Quantity",
    font=("Arial", 11, "bold"),
    bg=BG,
    fg=NAVY,
    padx=8,
    pady=5
)
quantity_frame.pack(fill="x", padx=5, pady=3)

# Quantity label and spinbox
quantity_row = tk.Frame(quantity_frame, bg=BG)
quantity_row.pack(anchor="center", pady=3)

tk.Label(
    quantity_row,
    text="Quantity:",
    font=("Arial", 10),
    bg=BG,
    fg=NAVY
).pack(side="left", padx=5)

quantity_box = tk.Spinbox(
    quantity_row,
    from_=1,
    to=20,
    width=5,
    font=("Arial", 10)
)
quantity_box.pack(side="left", padx=5)

# Add to Order button below quantity
add_button = tk.Button(
    quantity_frame,
    text="Add to Order",
    command=add_to_order,
    bg=BLUE,
    fg=WHITE,
    font=("Arial", 10, "bold"),
    padx=12,
    pady=3
)
add_button.pack(pady=3)

# ---------------- RUN APPLICATION ----------------

root.mainloop()
