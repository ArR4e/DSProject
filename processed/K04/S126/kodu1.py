š = 0.06
p = 0.04
n = 0.10
kooginimi = input("Sisestage koogi nimi: ")
koogimõõt = float(input("Sisestage koogimõõt: "))
def koogi_hind (x, y):
    if (x == 'Napoleoni'):
        hind = y**2 * n
        maksumus = round(hind, 2)
        print("Napoleoni koogi maksumus on: " + str(maksumus))
    elif (x == "šokolaadi" or (x == "ploomi")):
        if x == "šokolaadi":
            hind2 = math.pi * (y**2) * š
            maks = round(hind2, 2)
            print("Šokolaadikoogi maksumus on: " + str(maks))
        elif x == "ploomi":
            hind3 = math.pi * (y**2) * p
            maksmine = round(hind3, 2)
            print("Ploomikoogi maksumus on: " + str(maksmine))
            
try:
    koogid =["Napoleoni", "šokolaadi", "ploomi"]
    if kooginimi in koogid:
        koogihind(kookinimi, koogimõõt)
    if not kooginimi in koogid:
        raise ValueError
except:
    print("Sellist kooki andmebaasist ei leitud.")