from math import pi

def koogi_hind(nimi,mõõt):
    if nimi.lower() == "šokolaadikook":
        return round((pi*mõõt**2)*0.06,2)
    elif nimi.lower() == "ploomikook":
        return round((pi*mõõt**2)*0.04,2)
    elif nimi.lower() == "napoleoni kook":
        return round(mõõt**2*0.1,2)
    else:
        print("Sellise nimega kooki ei ole")

kook = input("Sisesta koogi nimi: ")
mõõt = float(input("Sisesta koogi mõõt: "))

if kook.lower() == "šokolaadikook" or kook.lower() == "ploomikook" or kook.lower() == "napoleoni kook":
    print(koogi_hind(kook,mõõt),"eurot")