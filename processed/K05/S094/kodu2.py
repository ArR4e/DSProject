
from random import choice

punct = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
# 32 märki

def suurväike(sone):
    for l in sone:
        if l.isupper():
            v = l.lower()
        elif l.islower():
            v = l.upper()
        elif l in punct:
            # kirjavahemark vahetus
            v = l.replace(l, rnd)
        elif l == " ":
            v = " "
        
        print(v, end="")
            
rnd = choice(punct)
suurväike("AbCdEfGhIjKlMnOpQrStUvWxYz")