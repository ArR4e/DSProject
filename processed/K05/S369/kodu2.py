import string
import random

symbol = string.punctuation
m2rk = symbol[random.randint(0, len(symbol)-1)]

def suurväike(lause):
    for i in lause:
        
        # kontrollime kas i on symbol
        if i in symbol:
            lause = lause.replace(i, m2rk)
            #lause = lause.replace(i, symbol[random.randint(0, len(symbol))])
            
    # Muudame vaiksed tahed suurteks ja vastupidi
    return lause.swapcase()
            

print(suurväike("Aias sadas saia, Leiba ja Peedi-Porgandi pehmikut."))

    