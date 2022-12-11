import string
import random

lause=input("Sisesta lause: ")
märk=string.punctuation
uus_märk=random.choice(märk)

def suurväike(lause):
    lause=lause.swapcase()
    for i in lause:
        if i in string.punctuation:
            lause=lause.replace(i, uus_märk) #miks ei?
    return lause

print(suurväike(lause))
