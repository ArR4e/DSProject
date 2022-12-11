##Pagarikoda valmistab kolme sorti kooke: šokolaadikook (0,06 €/cm2), ploomikook (0,04 €/cm2) ja Napoleoni kook (0,10 €/cm2).
##Kirjuta funktsioon koogi_hind, mis võtab argumentideks koogi nime ning mõõdu ja tagastab koogi maksumuse eurodes, ümardatult teise komakohani.
##Šokolaadikook ja ploomikook on ringikujulised ning etteantav mõõt tähistab raadiust. Napoleoni kook on ruudukujuline ning etteantav mõõt tähistab küljepikkust.
##Kui vastavat kooki funktsioonis ei leidu, tuleb visata erind sõnumiga „Sellist kooki andmebaasist ei leitud”.
##Seejärel kirjuta programm, mis küsib kasutajalt koogi nime ja mõõdu, arvutab funktsiooni koogi_hind abil selle koogi hinna ning väljastab tulemuse ekraanile.
##Küsimust korratakse, kuni kasutaja koogi nime sisestamata jätab ja Enter-klahvi vajutab.
##Automaatkontroll. Funktsiooni nimi peab olema koogi_hind, selle esimene parameeter on koogi nimi (sobivad väärtused "šokolaadikook", "ploomikook" ja "Napoleoni kook") ning
##teine parameeter koogi mõõt ujukomaarvuna. Juhul, kui esimese parameetri väärtus on midagi muud kui ülal loetletud, peab funktsioon genereerima erindi "Sellist kooki andmebaasist ei leitud".
##Funktsiooni tagastatav väärtus peab olema ümardatud kahe komakohani. Põhiprogrammis tuleb kasutajalt küsida andmeid samas järjekorras nagu funktsiooni parameetrid.###
from math import *

def koogi_hind(koogi_nimi, mõõt):
    if koogi_nimi == "šokolaadikook":
        return round(0.06 * (mõõt**2 * pi), 2)
    elif koogi_nimi == "ploomikook":
        return round(0.04 * (mõõt**2 * pi), 2)
    elif koogi_nimi == "Napoleoni kook":
        return round(0.1 * (mõõt**2), 2)
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")
        
kook = input("Sisesta koogi nimi: ")

while kook != "":
    koogi_mõõt = float(input("Sisesta koogi mõõt: "))
    print(koogi_hind(kook, koogi_mõõt))
    kook = input("Sisesta koogi nimi: ")