
def add_item(orders, item_name, price, quantity):
    total = price * quantity

    order = [item_name, price, quantity, total]
    orders.append(order)


def calculate_subtotal(orders):
    subtotal = 0

    for order in orders:
        subtotal = subtotal + order[3]

    return subtotal


def calculate_gst(subtotal):
    gst = subtotal * 18 / 100
    return gst



def generate_bill(orders):
    subtotal = calculate_subtotal(orders)
    gst = calculate_gst(subtotal)
    grand_total = subtotal + gst

    bill = ""
    bill += "=" * 55 + "\n"
    bill += "                 CAFE BILL\n"
    bill += "=" * 55 + "\n"
    bill += "{:<25} {:>8} {:>5} {:>10}\n".format(
        "Item", "Price", "Qty", "Total"
    )
    bill += "-" * 55 + "\n"

    for order in orders:
        name, price, quantity, total = order

        bill += "{:<25} {:>8} {:>5} {:>10}\n".format(
            name, price, quantity, total
        )

    bill += "-" * 55 + "\n"
    bill += "{:<38} {:>15.2f}\n".format("Subtotal (Rs.)", subtotal)
    bill += "{:<38} {:>15.2f}\n".format("GST (18%) (Rs.)", gst)
    bill += "-" * 55 + "\n"
    bill += "{:<38} {:>15.2f}\n".format("GRAND TOTAL (Rs.)", grand_total)
    bill += "=" * 55 + "\n"
    bill += "          Thank You! Visit Again!\n"
    bill += "=" * 55

    return bill
