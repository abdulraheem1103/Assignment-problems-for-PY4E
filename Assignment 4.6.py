def computepay(h,r):
    if h < 40:
        return None
    else:
        return r * 40 + (r * 1.5 * (h - 40) )

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate: ")
r = float(rate)
p = computepay(h,r)
print(p)
