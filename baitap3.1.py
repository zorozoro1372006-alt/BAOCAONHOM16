a=float(input("Enter Hours:"))
b=float(input("Enter Rate:"))
print("Enter Huors:",a)
print("Enter Rate:",b)
if a>40:
    c=40*10+(a-40)*15
else:
    c=a*b
print("Pay:",c)
