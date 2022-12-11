from math import pi

ümarkook = {"šokolaadikook" : 0.06, "ploomikook" : 0.04}
ruutkook = {"napoleoni kook" : 0.1}

def koogi_hind(külg, lisa):
    return külg ** 2 * lisa

while True:
    kook = input("Sisesta kook: ")
    kook = kook.lower()
    if kook in ümarkook or kook in ruutkook:
        mõõt = float(input("Sisesta koogi mõõt: "))
        if kook in ümarkook:
            print(float(round(koogi_hind(mõõt, pi) * ümarkook[kook], 2)))
        elif kook in ruutkook:
            print(float(round(koogi_hind(mõõt, 1) * ruutkook[kook], 2)))
    elif kook == "":
        break
    else:
        print("Sellist kooki andmebaasist ei leitud")