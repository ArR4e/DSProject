from string import*
from random2 import randint   
def suurväike(sona):
    tekst=""
    for taht in sona:
        if taht.islower():
            tekst=tekst+taht.upper()
        elif taht.isupper():
            tekst=tekst+taht.lower()
        elif taht in punctuation:
            tekst=tekst+punctuation[randint(1,32)]
        else:
            tekst=tekst+taht
    return tekst
