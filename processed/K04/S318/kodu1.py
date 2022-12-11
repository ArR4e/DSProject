from math import pi

while True:
    k_nim = input("Sisesta koogi nimi: ")
    if k_nim == "":
        break
    k_moot = input("Sisesta koogi mõõt (cm): ")
    def koogi_hind(nim,moot):
        if nim == "šokolaadikook":
            hind = pi*(float(moot)**2)*0.06
            return round(hind,2)
        elif nim == "ploomikook":
            hind = pi*(float(moot)**2)*0.04
            return round(hind,2)
        elif nim == "Napoleoni kook":
            hind = (float(moot)**2)*0.1
            return round(hind,2)
        else:
            raise VallueError("Sellist kooki andmebaasist ei leitud")
    print("Koogi hind on: "+str(koogi_hind(k_nim,k_moot))+"eurot.")

