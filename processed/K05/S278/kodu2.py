# Vihje: >>> string.punctuation '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
import random
import string
def suurväike(sõne):
    muudetud_sõne = []
    muudetud_sõne =sõne.swapcase()
    punc = list(string.punctuation)
    random.shuffle(punc)
    ransum = punc [0]
    for sym in sõne:
        if sym in string.punctuation:
            sym = ransum
        else:
            sym.swapcase()
    muudetud_sõne+=sym
    muudetud_sõne= ''.join(muudetud_sõne)
    return muudetud_sõne
print(suurväike("DFFGF..,gggh"))