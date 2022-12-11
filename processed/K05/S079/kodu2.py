# 2. Suured väikeseks ja väikesed suureks
# Kirjuta funktsioon suurväike, mis võtab argumendiks mingi sõne ning tagastab sõne järgmisel kujul:

# suured tähed on muudetud väikeseks;
# väikesed tähed on muudetud suureks;
# kõik kirjavahemärkide sümbolid on asendatud mingi ühe ja sama juhusliku kirjavahemärgisümboliga.
# Näide:

# >>> suurväike("MinA oleN Tubli!!")
# 'mINa OLEn tUBLI##'
 
# >>> suurväike("Aias sadas saia, Leiba ja Peedi-Porgandi pehmikut.")
# 'aIAS SADAS SAIA& lEIBA JA pEEDI&pORGANDI PEHMIKUT&'

#Vihje:
# >>> string.punctuation
# '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

# Automaatkontroll. Funktsiooni nimi peab olema suurväike ja sellel funktsioonil peab olema täpselt üks argument, mis on sõne.
# Funktsioon peab tagastama sõne, kus kõik antud sõne suured tähed on asendatud väikestega,
# väikesed tähed suurtega ja kõik kirjavahemärkide sümbolid asendatud teatud juhuslikult valitud kirjavahemärgisümboliga.

import random
import string

def suurväike(sõne):
    rndm = random.choice(string.punctuation)
    
    uus_sõne = ""
    for s in sõne:
        if s.isupper():
            s = s.lower()
            uus_sõne += s
        elif s.islower():
            s = s.upper()
            uus_sõne += s
        elif s.isnumeric():
            uus_sõne += s
        elif s == " ":
            uus_sõne += s
        else:
            s = rndm
            uus_sõne += s
    return uus_sõne