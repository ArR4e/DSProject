from math import *

aastatulu = float(input("Sisesta oma aastatulu: "))
 
if aastatulu > 6000:
    if aastatulu <= 14400:
        print("Maksuvaba tulu on 6000€.")
    else:
        if aastatulu <= 25200:
            valem = 6000 - 6000 / 10800 * (aastatulu - 14400)
            a = round(valem, 2)
            print("Maksuvaba tulu on " + str(a) + "€.")
        else:
            print("Maksuvaba tulu on 0€.")
else:
    print("Maksuvaba tulu on " + str(aastatulu) + "€.")