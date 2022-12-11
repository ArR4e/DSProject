#Pagarikoja kassaaparaat
from math import pi

def ring(z):
    return z**2 * pi

def koogi_hind(x, y):
    if x == "šokolaadikook":
        return round(ring(y)*0.06, 2)
    if x == "ploomikook":
        return round(ring(y)*0.04, 2)
    if x == "Napoleoni kook":
        return round(y**2*0.1, 2)

while True:
    a=input("Sisesta koogi nimi: ")
    if a=="":
        break
    b=float(input("Sisesta koogi mõõtmed: "))
    try:
        print("Koogi hind on", float(koogi_hind(a, b)), "eurot.")
    except:
        print("Sellist kooki andmebaasis ei leidu.")
