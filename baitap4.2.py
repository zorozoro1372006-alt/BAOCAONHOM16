a=input("Enter score:")
def computegrade(b):
         print("Enter score:",b)
         if 0>b or b>1:
             return ("Bad score.")
         elif b>0.9:
              return ("A")
         elif b>0.8:
              return("B")
         elif b>0.7:
              return("C")
         elif b>0.6:
              return("D")
         else:
             return("F")
try:
    b=float(a)
    print(computegrade(b))
except:
     print("Enter score:",a)
     print("Bad score.")
     