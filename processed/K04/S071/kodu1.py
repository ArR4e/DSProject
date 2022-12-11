# šokolaadikook (0,06 €/cm2), ploomikook (0,04 €/cm2) ja Napoleoni kook (0,10 €/cm2)
# Šokolaadikook ja ploomikook on ringikujulised ning etteantav mõõt tähistab raadiust.
# Napoleoni kook on ruudukujuline ning etteantav mõõt tähistab küljepikkust.
# Kui vastavat kooki funktsioonis ei leidu, tuleb visata erind sõnumiga „Sellist kooki andmebaasist ei leitud”.

#Seejärel kirjuta programm, mis küsib kasutajalt koogi nime ja mõõdu, arvutab funktsiooni koogi_hind abil selle koogi hinna ning väljastab tulemuse ekraanile.
#Küsimust korratakse, kuni kasutaja koogi nime sisestamata jätab ja Enter-klahvi vajutab.

from math import *

def koogi_hind(nimi,mõõt):
    if nimi == "šokolaadikook":
        raadius = mõõt
        hind = (pi * (raadius * raadius)) * 0.06
        
    elif nimi =="ploomikook":
        raadius = mõõt
        hind = (pi * (raadius * raadius)) * 0.04
        
    elif nimi == "Napoleoni kook":
        küljepikkus = mõõt
        hind = (küljepikkus * küljepikkus) * 0.10

    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")
    return(round(hind,2))
    
nimiNOPE = ""
while True:
    nimi = input("Koogi nimi: ")
    if nimi == nimiNOPE:
        break
    else:
        mõõt = float(input("Koogi mõõt: "))
        print(koogi_hind(nimi,mõõt))
