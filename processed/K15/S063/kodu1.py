'''-- Kodutöö nr. 15 - 1. Regulaaravaldis --'''
####################################################################
## Programm otsib failist üles read, milles esinevad TÜ kasutajanime
## sisaldavad veebiaadressid ning väljastab kasutajanimed ekraanile.
import re

f = open("aadressid.txt")

# kasutajanime muster '~<kasutajanimi>'
muster = r"~\S+"

for rida in f:
    # kui veebiaadress on tü serveri aadress
    if re.search("(https?)://(www)?.?(ut.ee)/~", rida):
        rida = rida.split("/")
        for r in rida:
            # vastavad mustrile alamsõned reas
            kasutajanimi = re.findall(muster, r)
            # kui pole tühi, siis väljasta
            if kasutajanimi:
                print(kasutajanimi[0].lstrip("~"))
f.close()
####################################################################