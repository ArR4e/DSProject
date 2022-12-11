from math import*

king=open("kinganumbrid.txt")
pikkus=0
for x in king:
    try:
        pikkus=2/3*(float(x)-2)
        print(round(pikkus))
    except:
        print("Vigane sisend.")
king.close()