import random
import string

def suurväike(s):
    s = s.swapcase()
    list = string.punctuation.split()
    for el in s:
        if el in list:
            el += random.choice(list)
    return s


lause = input("Sisestage soovitud lause: ")
print(suurväike(lause))
         