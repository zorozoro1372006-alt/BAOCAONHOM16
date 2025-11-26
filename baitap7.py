nums = []
while True:
    s = input("Enter a number: ")
    if s == "done":
        break
    try:
        num = float(s)
        nums.append(num)
    except:
        print("Invalid input")
print("Maximum:", max(nums))
print("Minimum:", min(nums))