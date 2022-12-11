from math import pi
def koogi_hind(nimi, mõõt):
    pindala = pi * mõõt ** 2
    hindkoogil = pindala * hind
    return round(hindkoogil, 2)
  
               
while True:
    nimi = input("Koogi nimi: ")
    if nimi == "":
        break
    if nimi == "šokolaadikook":
        hind = 0.06
    elif nimi == "ploomikook":
        hind = 0.04
    elif nimi == "Napoleoni kook":
        hind = 0.10
    else:
        raise ValueError("Sellist kooki andmebaasist ei leitud")
    mõõt = float(input("Koogi mõõt: "))
    print("Koogi hind on", koogi_hind(nimi, mõõt), "eurot.")





