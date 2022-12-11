import math
def koogi_hind(nimi, mõõt):
    nimi = nimi.lower()
    if nimi == "šokolaadikook" or "ploomikook" or "napoleoni kook":
        S = math.pi*mõõt**2
        if nimi == "šokolaadikook":
            hind = S*0.06
        elif nimi == "ploomikook":
            hind = S*0.04
        elif nimi == "napoleoni kook":
            S = mõõt**2
            hind = S*0.1
        hind = round(hind,2)
        print("Koogi hind ruutsentimeetri kohta on "+str(hind)+"€.")
    else:
       print("Andmebaasis puudub vastav kook.")
       Kook()
def Kook():
    while True:
        kook = input("Sisestage kook:")
        if kook == "":
            break
        koogi_mõõt = float(input("Sisestage koogi mõõt:"))
        if koogi_mõõt <= 0:
            print("Mõõt ei saa olla 0 ega sellest väiksem.")
        else:
            koogi_hind(kook,koogi_mõõt)
Kook()