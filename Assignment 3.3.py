try:
    score = input("Enter Score: ")
    s = float(score)
    if s > 1.0:
        print("Value out of range!")
    elif 1.0 >= s >= 0.9:
        print("A")
    elif 1.0 >= s >= 0.8:
        print("B")
    elif 1.0 >= s >= 0.7:
        print("C")
    elif 1.0 >= s >= 0.6:
        print("D")
    elif 1.0 >= s < 0.6:
        print("F")

except:
    print("Error, please re-enter the value")
