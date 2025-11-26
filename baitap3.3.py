a=input("Enter score:")
try:
    b=float(a)
    print("Enter score:",b)
    if 0>b>1:
        print("Bad score.")
    elif b>=0.9:
        print("A")
    elif b>=0.8:
        print("B")
    elif b>=0.7:
        print("C")
    elif b>=0.6:
        print("D")
    else:
        print("F")
except:
    print("Enter score:",a)                            
    print("Bad score.")