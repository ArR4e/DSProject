

cm2_hind=0
pindala=0
nimi=0
mõõt=0
x=0
def koogi_hind(nimi, mõõt):
    while True:
        nimi=input("Sisestage koogi nimi: ")
        if nimi=='':
            break
        mõõt=(input("Sisestage koogi mõõt: "))
        if nimi == "šokolaadikook":
            cm2_hind=0.06
            pindala=float(3.14159*(float(mõõt)**2))
        elif nimi == "Napoleonikook":
            cm2_hind=0.10
            pindala=((float(mõõt))**2)
        elif nimi == "ploomikook":
            cm2_hind=0.04
            pindala=float(3.14159*(float(mõõt)**2))
        else:
            raise Exception("Sellist kooki andmebaasist ei leitud")
        hind=round(pindala*cm2_hind,2)
        return hind
while True:
    x=koogi_hind(nimi,mõõt)
    if x== None:
        break
    else:
        print(x)
