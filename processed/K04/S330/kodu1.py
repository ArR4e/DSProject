from math import pi

koogid = ["šokolaadikook", "ploomikook", "Napoleoni kook"]

def koogi_hind(n, m):
    if n == "šokolaadikook":
        h = 0.06
        return round((pi * float(m) ** 2) * h, 2)
    elif n == "ploomikook":
        h = 0.04
        return round((pi * float(m) ** 2) * h, 2)
    elif n == "Napoleoni kook":
        return round((float(m) ** 2) * h, 2)
    
n = input("Sisestage koogi nimi: ")
while n not in koogid:
    print("Sellist kooki andmebaasist ei leitud")
    n = input("Sisestage koogi nimi: ")
while True:
    try:
        m = float(input("Sisestage koogi mõõt: "))
        print("Koogi hind on", koogi_hind(n, m), "eurot.")
        break
    except:
        print("Mõõtmed vales formaadis")
                  