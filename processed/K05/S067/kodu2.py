import string
import secrets
def suurväike(x):
    margid = []
    sõna = []
    for i in string.punctuation:
        margid.append(i)
    y = secrets.choice(margid)
    for sisu in x:
        if sisu.isalpha() == True and sisu == sisu.lower():
            uus = sisu.upper()
            sõna.append(uus)
            continue
        if sisu.isalpha() == True and sisu == sisu.upper():
            uus = sisu.lower()
            sõna.append(uus)
            continue
        if sisu in string.punctuation:
            uus = str(y)
            sõna.append(uus)
            continue
        if sisu == ' ':
            uus = ' '
            sõna.append(uus)
    return ''.join(sõna)
print(suurväike('asd,..,KSAD  Lssd,!!?dDSA'))