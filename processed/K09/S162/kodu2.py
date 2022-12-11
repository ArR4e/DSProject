from random import randint
def minu_shuffle(järjend):
    for el in järjend:
        vanakoht=järjend.index(el)
        uuskoht=randint(0,len(järjend)-1)
        hoiul=järjend[vanakoht]
        if vanakoht==uuskoht:
            continue
        else:
            järjend[vanakoht]=järjend[uuskoht]
            järjend[uuskoht]=hoiul
            print(järjend)
    