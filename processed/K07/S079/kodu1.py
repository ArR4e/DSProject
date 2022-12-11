# 1. Poiste ja tüdrukute arv
# Kirjuta funktsioon poisse_ja_tüdrukuid, mis võtab argumendiks järjendi,
# kus igal real on eesnimi (võib koosneda ka mitmest nimest) ning tühikuga eraldatud sugu
# (P poiste puhul ja T tüdrukute). Funktsioon peab tagastama kaheelemendilise enniku,
# mille esimene element on järjendis olevate poiste arv ning teine element on tüdrukute arv.
# Järjendit tuleks töödelda for-tsükliga.

# Näide

#  >>> poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T'])
# (3, 2)
# Automaatkontroll. Funktsiooni nimi peab olema poisse_ja_tüdrukuid ja sellel
# funktsioonil peab olema täpselt üks argument, järjend. Järjendis peab iga elemendi väärtus olema sõne,
# mis lõpeb kas tähega P või T, kusjuures sellele tähele eelneb tühik. Kõik, mis omakorda tühikule eelneb, loetakse nimeks.
# Järjendis võib poiste hulk või tüdrukute hulk olla tühi, samuti võib tühi olla ka terve järjend.
# Funktsioon peab tagastama paari (m,n), kus m ja n on mittenegatiivsed täisarvud. Kui poisse või tüdrukuid pole,
# siis on tagastatavas paaris vastav väärtus 0.


def poisse_ja_tüdrukuid(järjend):
    
    poisse = 0
    tüdrukuid = 0
    for i in järjend:
        if i[-1] == "P":
            poisse += 1
        if i[-1] == "T":
            tüdrukuid += 1
    
    kokku = (poisse, tüdrukuid)
    return kokku
