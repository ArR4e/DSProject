import string
import random

kirjavahemargid ='!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
uusKirjavahemark = ""
def suurväike(sõne):
    uusKirjavahemark = random.choice(kirjavahemargid)
    vahetatudtekst = ""
    uusTekst = sõne.swapcase()
    for i in uusTekst:
       if i in kirjavahemargid:
            uusTekst = uusTekst.replace(i,uusKirjavahemark)
    
    return uusTekst
