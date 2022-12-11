import math
liin = int(input("Mitu meetrit pikk on teie soovitud elektriliin? "))
vahe = int(input("Mitu meetrit on maksimaalselt kahe posti vahel? (max 100m) "))
if vahe > 100:
    print("Teie postide vahed on liiga suured, valige midagi mis ei ületa 100m.")
elif vahe >= liin:
    print("Teil läheb liini püstitamiseks vaja minimaalselt 2 elektriposti.")
else:
    elektripostid_jääk = int(liin % vahe)
    if elektripostid_jääk > 0:
        elektripostid = str(int(liin / vahe + 2))
    else:
        elektripostid = str(int(liin / vahe + 1))
    print("Teil läheb liini püstitamiseks vaja minimaalselt " + elektripostid + " elektriposti.")
