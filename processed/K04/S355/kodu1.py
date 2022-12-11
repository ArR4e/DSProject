import math

def koogi_hind(kooginimi, koogi_mõõt):
    
    if kooginimi == "ploomikook":
        koogi_S = math.pi*koogi_mõõt*koogi_mõõt
        maksumus = str(round((koogi_S * ploom_hind), 2))
        print("Ploomikoogi tüki hind on " + maksumus + " eurot")
    elif kooginimi == "Napoleoni kook":
        koogi_S = koogi_mõõt*koogi_mõõt
        maksumus = str(round((koogi_S * nap_hind), 2))
        print("Napoleoni tüki hind on " + maksumus + " eurot")
    elif kooginimi == "ðokolaadikook":
        koogi_S = math.pi*koogi_mõõt*koogi_mõõt 
        maksumus = str(round((koogi_S * sok_hind), 2))
        print("Sokolaadikoogi tüki hind on " + maksumus + " eurot")
    else:
        print("Sellist kooki andmebaasist ei leitud")
        
nap_hind = 0.1
ploom_hind = 0.04
sok_hind = 0.06
kooginimi = " "
koogi_mõõt = 0 

while True:
    if kooginimi != "":
        kooginimi  = input("Mis kooki sa soovid? ")
        koogi_mõõt = float(input("Kui suurt koogitükki sa soovid? (cm) "))
        koogi_hind(kooginimi, koogi_mõõt)
        