def computepay(a, b):
    if a > 40:
        c = 40 * b + (a - 40) * b * 1.5
    else:
        c = a * b
    return c

a = float(input("Enter Hours:"))
b = float(input("Enter Rate:"))
print("Ennter Hours:", a)
print("Enter Rate:", b)
print("Pay:", computepay(a, b))