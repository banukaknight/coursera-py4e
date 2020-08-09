largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try :
        n = int(num)
    except :
        print("Invalid input")
    if largest is None:
        largest = smallest = n
    if largest < n:
        largest = n
    if smallest > n:
        smallest = n

print("Maximum is", largest)
print("Minimum is", smallest)
