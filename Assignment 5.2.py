largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
   
    try :
        num = int(num)   #Used this try/except to check wheather the given input is a integer or not
    except :
        print ("Invalid input")
        continue
    
    if num > largest :
        largest = num
    if smallest is None :
        smallest = num
    elif num < smallest :
        smallest = num

print("Maximum is", largest)
print ("Minimum is", smallest)
