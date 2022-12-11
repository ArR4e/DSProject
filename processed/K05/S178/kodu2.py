import random
import string


def suurväike(algne):
    parast1 = str(algne.swapcase())
    parast2 = str(parast1)
    margid = string.punctuation
    e = random.choice(string.punctuation)
    for c in margid:
        parast2 = parast2.replace(c, e)
    return(parast2)

algne = str(input('Sisesta sõna, mida soovid muuta: '))

print(suurväike(algne))