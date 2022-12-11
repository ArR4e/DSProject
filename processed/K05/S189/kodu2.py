import string
from random import randint

def suurväike(lause):
    uus_lause = lause.swapcase()
    sümbolid = string.punctuation
    juhuslik = sümbolid[randint(0, len(sümbolid)-1)]
    for i in range(len(uus_lause)):
        if uus_lause[i] in sümbolid:
            uus_lause = uus_lause.replace(uus_lause[i], juhuslik)
    return uus_lause

lause = input("Sisesta lause: ")
print(suurväike(lause))
    