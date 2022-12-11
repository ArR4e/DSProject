import math

def koogi_hind(nimi, r):
    if nimi.lower() == "šokolaadikook":
        hind = round((((math.pi*r*r)/2)*0.06), 2)
        return(hind)
    elif nimi.lower() == "ploomikook":
        hind = round((((math.pi*r*r)/2)*0.04), 2)
        return(hind)
    elif nimi.lower() == "napoleoni kook":
        hind = round((r*r), 2)
        return(hind)

while True:
    a = input("Sisesta koogi nimi: ")
    b = float(input("Sisesta koogi mõõt (cm): "))
    if a != "šokolaadikook" and a != "ploomikook" and a != "napoleoni kook":
        print("Sellist kooki andmebaasist ei leitud.")
        continue
    elif a == "":
        break
    print(koogi_hind(a, b))