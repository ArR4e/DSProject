#mirjampirn
aastatulu=float(input("Palun sisestage oma aastatulu: "))

if aastatulu<6000 or aastatulu==6000:
    print("Teie maksuvaba tulu on: " + str(aastatulu) , (" eurot"))
elif aastatulu>6000 and aastatulu<14399:
    print("Teie maksuvaba tulu on 6000 eurot")
aastatuluvalem= 6000-6000/10800*(aastatulu-14400)
if aastatulu>14400 and aastatulu<25200 or aastatulu==14400 or aastatulu==25200:
    print("Teie maksuvaba tulu on " + str(round(aastatuluvalem,2)) ,  "eurot")
if aastatulu>25200:
    print("Teie maksuvaba tulu on 0 eurot")