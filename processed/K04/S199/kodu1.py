from math import pi

def koogi_hind(koogi_nimi, mõõt):
    if koogi_nimi != "ðokolaadikook" or  koogi_nimi != "ploomikook" or koogi_nimi != "Napoleoni kook":
        raise Exception("Sellist kooki andmebaasist ei leitud")

    if koogi_nimi == "ðokolaadikook":
        pindala = pi * mõõt ** 2
        maksumus = round(0.06 * pindala, 2)
    else:
        if koogi_nimi == "ploomikook":
            pindala = pi * mõõt ** 2
            maksumus = round(0.04 * pindala, 2)
        else:
            pindala = mõõt ** 2
            maksumus = round(0.10 * pindala, 2)
  
  
    print("Kook maksab", maksumus, "eurot.")

while True:
    koogi_nimi = str(input("Sisestage koogi nimi(programmi lõpetamiseks vajutage ENTER): "))
    if koogi_nimi == "":
        break
    else:
        if koogi_nimi == "ðokolaadikook" or koogi_nimi == "ploomikook":
            mõõt = float(input("Sisestage koogi raadius: "))
        else:
            mõõt = float(input("Sisestage koogi lüljepikkus: "))
                
    koogi_hind(koogi_nimi, mõõt)
