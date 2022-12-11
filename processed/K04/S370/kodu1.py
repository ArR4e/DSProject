from math import *
def koogi_hind(ni, d):
    if ni=="šokolaadikook":
        return round((pi*(d/2)**2*0.06), 2)
    if ni=="ploomikook":
        return round(pi*(d/2)**2*0.04, 2)
    if ni=="Napoleoni kook":
        return round(d**2*0.1, 2)
    else:
        raise Exception("Sellist kooki andmebaasis ei leidu")
a=0
while True:
    a=input("Mis kooki soovid? Valikus on šokolaadikook, ploomikook ja Napoleoni kook.")
    if a== "":
        break
    b=float(input("Mis läbimõõduga kooki soovid?"))
    

    print("Koogi hind on", koogi_hind(a, b), "eurot.")