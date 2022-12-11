print("Tere, kallis kasutaja")
print("Palun sisestage oma aastane sissetulek (mittenegatiivne ujukomaarv), ning ma arvutan ja kuvan sinu maksuvaba tulu.")

from math import*

aastatulu = float(input("Palun sisestage aastatulu: "))

if aastatulu < 0:
    print("Sul on vale aastane sissetulek.")
    print("Palun sisestage see uuesti.")
else:
    if aastatulu <= 6000:
        a1 = round(aastatulu,2)
        print(a1)
    else:
        if aastatulu > 6000 and aastatulu <= 14400:
            a1 = round(aastatulu*0 + 6000,2)
            print(a1)
        else:
            if aastatulu > 14400 and aastatulu <= 25200:
                a1 = round(6000 - 6000 / 10800 * (aastatulu - 14400),2)
                print(a1)
            elif aastatulu > 25200:
                a1 = 0
                print(a1)
