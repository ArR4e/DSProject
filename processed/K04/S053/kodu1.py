from math import *

def koogi_hind(kooginimi, koogimõõt):
    while True:
        if kooginimi == "šokolaadikook":
            return (round((pi*koogimõõt**2)*0.06, 2))
        elif kooginimi == "ploomikook":
            return (round((pi*koogimõõt**2)*0.04, 2))
        elif kooginimi == "Napoleoni kook":
            return (round((koogimõõt**2)*0.1, 2))
        elif kooginimi == "":
            break
        else:
            raise Exception("Sellist kooki andmebaasist ei leitud")
        
kooginimi = str(input("Sisesta kooginimi: "))
koogimõõt = float(input("Sisesta koogimõõt: "))

print("Koogi maksumus on " + str(koogi_hind(kooginimi, koogimõõt)) + " eurot.")