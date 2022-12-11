import random

def suurväike(sone):
    vahemärk = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    kindelvm = vahemärk[random.randint(1, len(vahemärk))]
    sone2 = ""
    for i in range (len(sone)):
        if sone[i].isupper():
            sone2 += sone[i].lower()
        elif sone[i].islower():
            sone2 += sone[i].upper()
        elif sone[i] in vahemärk:
            sone2 += sone[i].replace(sone[i], kindelvm)
        else:
            sone2 += sone[i]
    print(sone2)
suurväike(input())