# Suured väikseks ja väiksed suureks

from string import punctuation
from random import randint

def suurväike(sõne):
    uus_sõne = ''
    uus_kirjavahemärk = punctuation[randint(0, len(punctuation))] #Valib uue kirjavahemärgi
    
    for tähemärk in sõne:
        if tähemärk.isalpha() and tähemärk.islower():
            uus_sõne += tähemärk.upper()
        elif tähemärk.isalpha() and tähemärk.isupper():
            uus_sõne += tähemärk.lower()
        elif tähemärk in punctuation:
            uus_sõne += uus_kirjavahemärk
        else:
            uus_sõne += tähemärk
    return uus_sõne