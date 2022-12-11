#mirjampirn
def koogi_hind(kooginimi, moot):
    try:
        if kooginimi=="šokolaadikook":
            koogihind=moot*moot*3.14*0.06
        elif kooginimi=="ploomikook":
            koogihind=moot*moot*3.14*0.04
        elif kooginimi=="Napoleoni kook":
            koogihind=moot*moot*0.1
        return print("Koogi hind on "+str(round(koogihind,2))+ " eurot")
    except:
        return print("Sellist kokki andmebaasist ei leitud!")

kooginimi=input("Palun sisestage kooginimi: ")

while kooginimi!="":
    moot=float(input("Palun sisestage koogimõõt (cm): "))
    koogi_hind(kooginimi,moot)
    kooginimi=input("Palun sisesta kooginimi: ")