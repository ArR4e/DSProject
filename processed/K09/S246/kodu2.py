from random import randint
def minu_shuffle(jarjend):
    pikkus = len(jarjend)
    tulemus = []
    for el in jarjend:
        suvaline1 = randint(0, pikkus - 1)
        suvaline2 = randint(0, pikkus - 1)
        segatud = jarjend[suvaline1], jarjend[suvaline2] = jarjend[suvaline2], jarjend[suvaline1]
        nimekiri = list(segatud)
        tulemus.append(nimekiri)