# 1. Regulaaravaldis
# Tartu ülikoolis on igal arvutivõrgu kasutajal oma kodukataloog. Sinna võib kasutaja luua oma kodulehe, mis asub ülikooli serveris.
# Koduleht on juurdepääsetav aadressilt http://www.ut.ee/~kasutajanimi/, näiteks http://www.ut.ee/~vilo.

# Faili aadressid.txt on salvestatud veebiaadressid, iga aadress eraldi real.
# Lisaks võib failis olla muud selgitavat teksti. Kirjuta programm, mis loeb faili sisse, otsib üles read,
# milles esinevad Tartu ülikooli kasutajanime sisaldavad veebiaadressid ning väljastab kasutajanimed ekraanile.
# Kasutajanimede otsimiseks veebiaadressidest tuleb kasutada regulaaravaldisi. Muu informatsiooni,
# sealhulgas muudel veebiaadressidel asuvad kasutajanimed, peaks programm vahele jätma.

# Kui näiteks faili aadressid.txt sisu on

# http://www.ut.ee/~koit/KT/index_eng.html
# Loeng kestab 90 minutit.
# http://butler.cc.tut.fi/~jorma/
# https://www.ut.ee/et/oppimine
# http://www.ut.ee/~vilo/
# http://www.ut.ee/~kiho/
# Kirjutis "x ~ y" tähendab, et x ja y on sama järku suurused.
# siis peaks programmi väljund olema

 # Kasutajanimed on:
 # koit
 # vilo
 # kiho
import re
f = open("aadressid.txt")

print("Kasutajanimed on: ")
for rida in f:
    rida = rida.strip()
    nimi = re.search("://www.ut.ee/~[a-ü]", rida)
    if nimi != None:
        r1 = rida.split("/~")[1].split("/")[0]
        print(r1)
    else:
        pass

f.close()
