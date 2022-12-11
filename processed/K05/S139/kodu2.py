import string
import random

def suurväike(lause):
    uus_märk = random.choice(string.punctuation)
    uus_sõne = ""
    for i in lause:
        if i in string.punctuation:
            i = uus_märk
            uus_sõne += i
        else:
            uus_sõne += i.swapcase()
    return uus_sõne

suurväike("Tere!,..--- PROGRAMeerija!?*`#%")