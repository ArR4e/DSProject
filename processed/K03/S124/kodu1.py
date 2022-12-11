from math import *

a = float(input("Sisesta aastatulu: "))
if a <= 6000:
    print(("Maksuvaba tulu on ") + str(a) + (" eurot."))
if a > 6000:
    if a <= 14400:
        print("Maksuvaba tulu on 6000 eurot aastas.")
if a > 14400:
    if a <= 25200:
        b = 6000 - 6000 / 10800 * (a - 14400)
        print(("Maksuvaba tulu on ") + str(round(b, 2)) + (" eurot."))
if a > 25200:
    print("Maksuvaba tulu on 0 eurot.")
    
#else?
              
        
