import math

def koogi_hind(x, y):
    if x == "Napoleoni kook":
        hind2 = round((y**2)*0.1), 2)
        return hind2
    elif x == "šokolaadikook":
        hind3 = round(((math.pi*(y**2))*0.06), 2)
        return hind3
    elif x == "ploomikook":
        hind4 = round(((math.pi*(y**2))*0.04), 2)
        return hind4
    else:
        print("Sellist kooki andmebaasist ei leitud.")
        

while True:
    x = str(input("Sisesta koogi nimi: "))
    if x == "":
        break
    else:
        y = float(input("Sisesta koogi mõõt: "))
        print("Kook maksab " + str(koogi_hind(x, y)) + "€")
        
