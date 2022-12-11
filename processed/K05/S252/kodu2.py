import string
import random

def asendaKirjavaheMargid(sisendString):
    kirjavahemargid = string.punctuation
    pikkus = len(kirjavahemargid)
    suvalineSymboliAsukoht = random.randrange(1,pikkus)
    suvalineSymbol = kirjavahemargid[suvalineSymboliAsukoht]
    result = ""
    for c in sisendString:
        if c in kirjavahemargid:
            result +=suvalineSymbol
        else:
            result += c
    return result  

def suurväike(sone):
    uusone = ""
    for i in range (len(sone)):
        if sone[i].isupper():
            uusone+=sone[i].lower()
        elif sone[i].islower():
            uusone+=sone[i].upper()
        else:
            uusone+=sone[i]

    uusone = asendaKirjavaheMargid(uusone)
    return uusone

sone = str(input("Siesta sõne:"))
uusSone = suurväike(sone)

print ("Asendatud tekst:" + uusSone)