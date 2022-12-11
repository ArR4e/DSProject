###############################################################################################################
## Kirjuta funktsioon poisse_ja_tüdrukuid, mis võtab argumendiks järjendi, kus igal real on eesnimi           #
## (võib koosneda ka mitmest nimest) ning tühikuga eraldatud sugu (P poiste puhul ja T tüdrukute).            #
## Funktsioon peab tagastama kaheelemendilise enniku, mille esimene element on järjendis olevate poiste arv   #
## ning teine element on tüdrukute arv. Järjendit tuleks töödelda for-tsükliga.                               #
###############################################################################################################
def poisse_ja_tüdrukuid(järjend):
    # esialgsed väärtused
    tüdrukuid = 0
    poisse = 0
    
    # iga sõne kohta järjendist
    for sõne in järjend:
        # eemaldame liigseid tühikuid sõne alguses ja lõpus
        sõne = sõne.strip()
        # võtame viimast elementi sõnest (peab olema kas P või T)
        sugu = sõne[len(sõne)-1]
        # kui T, siis lisame tüdrukute arvule veel 1
        # vastasel juhul lisame poiste arvule veel 1
        if sugu == "T":
            tüdrukuid += 1
        else:
            poisse += 1
    
    # tagastame ennikut (poiste arv, tüdrukute arv)
    return (poisse, tüdrukuid)
###############################################################################################################