from math import *

aastatulu = float(input("Palun sisestage Teie aastatulu: "))
arv1 = float(aastatulu)
arv2 = float(6000 - 6000 / 10800 * (aastatulu - 14400))

if aastatulu <= 6000:
    print("Maksuvaba tulu on:", arv1)
    
elif aastatulu <=14400:
    print("Maksuvaba tulu on 6000.0 eurot")
    
elif aastatulu <= 25200:
    print("Maksuvaba tulu on: ", 6000 - 6000 / 10800 * (aastatulu - 14400))
    
    round(6000 - 6000 / 10800 * (aastatulu - 14400),2)

else: print("Maksuvaba tulu on 0 ")


             
             








