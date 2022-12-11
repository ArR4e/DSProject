'''
Kirjuta funktsioon suurväike, mis võtab argumendiks mingi sõne ning tagastab sõne järgmisel kujul:

suured tähed on muudetud väikeseks;
väikesed tähed on muudetud suureks;
kõik kirjavahemärkide sümbolid on asendatud mingi ühe ja sama juhusliku kirjavahemärgisümboliga.
'''
import string
import random

def suurväike(sone):
    # esialgu teisendatud sone on tühi
    teisendatud = ""
    
    # kirjavahemärkide nimekiri
    kirjavahemargid = string.punctuation
    # juhuslikult valitud kirjavahemärk
    juhuslik_kirjavahemark = random.choice(kirjavahemargid)
    
    # iga sone tähemargi jaoks
    for s in sone:
        # kui on väike, teisenda suureks
        if s.islower():
            s = s.upper()
        # kui on suur, teisenda väikeseks
        elif s.isupper():
            s = s.lower()
        # kui see tähemärk on kirjavahemärk, asenda juhuslikuks kirjavahemärgiks
        elif s in kirjavahemargid:
            s = juhuslik_kirjavahemark
        # lisa teisendatud tähemärk teisendatud sone sisse
        teisendatud += s
    
    return teisendatud