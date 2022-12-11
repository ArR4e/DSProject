# 1. Pagarikoja kassaaparaat
# Pagarikoda valmistab kolme sorti kooke: šokolaadikook (0,06 €/cm2), ploomikook (0,04 €/cm2) ja Napoleoni kook (0,10 €/cm2).

# Kirjuta funktsioon koogi_hind, mis võtab argumentideks koogi nime ning mõõdu ja tagastab koogi maksumuse eurodes,
# ümardatult teise komakohani. Šokolaadikook ja ploomikook on ringikujulised ning etteantav mõõt tähistab raadiust.
# Napoleoni kook on ruudukujuline ning etteantav mõõt tähistab küljepikkust. Kui vastavat kooki funktsioonis ei leidu,
# tuleb visata erind sõnumiga „Sellist kooki andmebaasist ei leitud”.

# Seejärel kirjuta programm, mis küsib kasutajalt koogi nime ja mõõdu,
# arvutab funktsiooni koogi_hind abil selle koogi hinna ning väljastab tulemuse ekraanile.
# Küsimust korratakse, kuni kasutaja koogi nime sisestamata jätab ja Enter-klahvi vajutab.

# Automaatkontroll. Funktsiooni nimi peab olema koogi_hind, selle esimene parameeter on koogi nimi
# (sobivad väärtused "šokolaadikook", "ploomikook" ja "Napoleoni kook") ning teine parameeter koogi mõõt ujukomaarvuna.
# Juhul, kui esimese parameetri väärtus on midagi muud kui ülal loetletud, peab funktsioon genereerima erindi
# "Sellist kooki andmebaasist ei leitud". Funktsiooni tagastatav väärtus peab olema ümardatud kahe komakohani.
# Põhiprogrammis tuleb kasutajalt küsida andmeid samas järjekorras nagu funktsiooni parameetrid.
from math import pi

def koogi_hind(koogi_nimi, koogi_mõõt):
    if koogi_nimi == "šokolaadikook":
        hind = round(pi * koogi_mõõt**2 * 0.06, 2)
        return hind
    if koogi_nimi == "ploomikook":
        hind = round(pi * koogi_mõõt**2 * 0.04, 2)
        return hind
    if koogi_nimi == "Napoleoni kook":
        hind = round(koogi_mõõt**2 * 0.10, 2)
        return hind
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")

nimi = input("Sisesta koogi nimi (või lõpetamiseks Enter): ")

while True:
    if nimi == "":
        break
    else:
        mõõt = float(input("Sisesta koogi mõõt: "))
        print(koogi_hind(nimi, mõõt))
        nimi = input("Sisesta koogi nimi (või lõpetamiseks Enter): ")