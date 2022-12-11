lapsed = "lapsed.txt"
nimed = "nimed.txt"
from functools import reduce
def seosta_lapsed_ja_vanemad(lapsed, nimed):
    vanjalap = open(lapsed, "r")
    nimed = open(nimed, "r")
    nimekiri1 = {}
    for rida in vanjalap:
        kiri = rida.strip().split()
        try:
            nimekiri1[kiri[1]] = nimekiri1.get(kiri[1]) + " "+ kiri[0]
        except:
            nimekiri1[kiri[1]] = kiri[0]
    for laps, vanemad in nimekiri1.items():
        uusvanemad = vanemad.split(" ")
        uusvanemad = set(uusvanemad)
        nimekiri1[laps] = uusvanemad
    print(nimekiri1)
    nimekiri2 = {}
    for rida in nimed:
        kiri = rida.strip().split()
        nimekiri2[kiri[0]] = kiri[1] + " " + kiri[2]
    print(nimekiri2)
    loppnimekiri = {}
    for laps, vanem in nimekiri1.items():
        laps = nimekiri2[laps]
        vanemad1 = set()
        for vane in vanem:
            vana = nimekiri2[vane]
            vanemad1.add(vana)
        loppnimekiri[laps] = vanemad1

    return(loppnimekiri)
        
seosta_lapsed_ja_vanemad(lapsed, nimed)