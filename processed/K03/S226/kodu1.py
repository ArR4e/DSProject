from math import*
#input data
aastatulu= float(input("Sisestage oma aastatulu: "))

#valemeraldi
kolmasaste = 6000 - 6000 / 10800 * (aastatulu - 14400)

#tingimused
if aastatulu < 6000:
    print("Teie maksevaba tulu on: ", aastatulu)
else:
    if aastatulu >= 6000 and aastatulu <= 14400:
        print("Teie maksevaba tulu on: 6000")
    else:
        if aastatulu >= 14400 and aastatulu <= 25200:
            print("Teie maksevaba tulu on:", round(kolmasaste, 2))
        else:
            if aastatulu > 25200:
                print("Teie maksevaba tulu on 0.")