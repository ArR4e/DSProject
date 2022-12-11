from math import pi

a = input("Sisesta koogi nimi: ")
b = float(input("Sisesta koogi mõõt: "))

def koogi_hind(a, b):
    while True:
        if a("šokolaadikook"):
            return round(0.06 * b**2, 2)
        elif a("ploomikook"):
            return round(0.04 * b**2, 2)
        elif a("Napoleoni kook"):
            return round(0.10 * pi * b**2, 2)
        elif a == "":
            break
        else:
            raise ValueError("Sellist kooki andmebaasist ei leitud.")
print("Koogi hind on", koogi_hind(a, b), "eurot.")