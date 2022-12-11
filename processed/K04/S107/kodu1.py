from math import pi
#mõõt = input("Sisesta koogi mõõt cm: ")
#nimi = input("Sisesta koogi nimi: ")

def koogi_hind(nimi, mõõt):

    if nimi == "Napoleoni kook":
        pindala = mõõt**2
        hind = round((pindala*0.10), 2)
        return hind
      #  print("Napoleoni koogi hind on", hind, "eurot.")
    elif nimi == "šokolaadikook":
        pindala = mõõt**2*pi
        hind = round((pindala*0.06), 2)
        return hind
       # print("Šokolaadikoogi hind on", hind, "eurot.")
    elif nimi == "ploomikook":
        pindala = mõõt**2*pi
        hind = round((pindala*0.04), 2)
        return hind
      #  print("Ploomikoogi hind on", hind, "eurot.")
    else:
        raise Exception ("Sellist kooki andmebaasist ei leitud")
while True:
    nimi = input("Sisesta koogi nimi: ")
    if nimi == "":
        break
    mõõt = float(input("Sisesta koogi mõõt cm: "))
  #  koogi_hind(nimi, mõõt)
    print("Koogi hind on:", koogi_hind(nimi, mõõt))