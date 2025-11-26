try:
    a = float(input("Enter Hours:"))
    b = float(input("Enter Rate:"))
    print("Enter Hours:", a)
    print("Enter Rate:", b)
    if a > 40:
        c = 40 * b + (a - 40) * 1.5 * b
    else:
        c = a * b
    print("Pay:", c)
except:
    print("Error, please enter numeric input")