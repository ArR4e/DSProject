from re import sub
from random import choice
from string import punctuation

def suurväike(sõne):
    märk = choice(punctuation)
    sõne = sub('[^a-zA-Z0-9õÕäÄöÖüÜ \n]', märk, sõne).swapcase()
    return sõne

sõne = input('Sisestage sõne: ')

print(suurväike(sõne))