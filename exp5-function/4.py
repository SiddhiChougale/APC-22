def interest(p, r, t):
    si = (p * r * t) / 100
    return si

p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

print("Simple Interest =", interest(p, r, t))
