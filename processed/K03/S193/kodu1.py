from math import*

aastatulu = (input("Palun sisestage oma aastatulu: "))
a = abs(float(aastatulu))

if a <= 6000:
    print("Maksuvaba tulu on: " + str(round(a, 2)))
        
else:
    if a > 6000 and a < 14400:
        print("Maksuvaba tulu on: 6000 ")
        

if a >= 14400 and a < 25200:
    print("Maksuvaba tulu on: " + str(round(6000 - 6000 / 10800 * (a - 14400),2)))

elif a >= 25200:
    print("Maksuvaba tulu on: 0")