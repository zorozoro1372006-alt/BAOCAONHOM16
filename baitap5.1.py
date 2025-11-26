a=0
b=0
while True:
    c=input("Enter a number:")
    if c == 'done':
     break
    try:
       d=float(c)
       a+=d
       b+=1
    except:
       print("Invalid input.")
       continue
    a=a+d
    b=b+1
e=a/b
print(a, b, e)

   
   
      


      
   
       
 

