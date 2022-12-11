from math import pi

def koogi_hind(a, b):
    if a == "šokolaadikook" or a == "ploomikook":
        suurus = pi * float(b)**2
        if a == "šokolaadikook":
            return round(suurus * 0.06, 2)
        elif a == "ploomikook":
            return round(suurus * 0.04, 2)
    elif a == "Napoleoni kook":
        suurus = b ** 2
        return round(suurus * 0.10, 2)
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud.")

def main():
    koogi_nimi = " "
    while(koogi_nimi != ""):
        koogi_nimi = input("Sisestage koogi nimi: ")
        if koogi_nimi == "šokolaadikook" or koogi_nimi == "ploomikook" or koogi_nimi == "Napoleoni kook":
            koogi_mõõt = input("Sisestage koogi küljepikkus/raadius: ")
            while(True):
                try:
                    koogi_mõõt = float(koogi_mõõt)
                    a = koogi_hind(koogi_nimi, koogi_mõõt)
                    print(a)
                    break
                except:
                    koogi_mõõt = input("Sisestage koogi küljepikkus/raadius ARVUNA: ")
        elif koogi_nimi == "":
            break
        else:
            koogi_hind(koogi_nimi, 0)
main()