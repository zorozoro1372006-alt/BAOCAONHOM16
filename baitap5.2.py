a= None
b= None
while True:
    c=input("Enter a number:")
    if c == 'done':
     break
    try:
       d=float(c)
    except:
       print("Invalid input.")
       continue
    if a is None or a<d:
       a=d
    if b is None or b>d:
       b=d
print("Maximum is",a)
print("Minimum is",b)         