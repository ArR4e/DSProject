import random
import string

märk = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

def suurväike(string):
    muudetud = string.swapcase()
    märkmuudetud = märk[random.randint(0, len(märk))]
    for i in range(len(märk)):
        if märk[i] in muudetud:
            muudetud = muudetud.replace(märk[i], märkmuudetud)
    return muudetud
    