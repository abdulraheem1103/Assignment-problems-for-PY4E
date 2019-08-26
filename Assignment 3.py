hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate")
r = float(rate)

if hrs <= 40 :
    pay = h * rate
else :
    pay = r * 40 + (r * 1.5 * (h - 40)) #this condition was given in the question

print (pay)
