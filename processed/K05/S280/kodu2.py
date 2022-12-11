# 2. Suured väikeseks ja väiksed suureks / RP
from random import randint
import string

special = []
for x in string.punctuation:
    special.append(x)

def suurväike(sõne):
    uus_sõna = ""
    suvaline = special[randint(0,len(special)-1)]
    for sõna in sõne:
        if sõna in special:
            sõna = suvaline
            uus_sõna += sõna
        elif sõna.islower() == False:
            sõna = sõna.lower()
            uus_sõna += sõna
        elif sõna.islower() == True:
            sõna = sõna.upper()
            uus_sõna += sõna

    return uus_sõna

lause = input("Sisesta lause: ")
print("Uus lause:",suurväike(lause))