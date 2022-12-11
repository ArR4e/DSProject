from random import randint
def minu_shuffle(jes):
    suva = len(jes)
    for el in jes:
        juhuslik = randint(0,suva-1)
        juhuslik2 = randint(0,suva-1)
        jes[juhuslik], jes[juhuslik2] = jes[juhuslik2], jes[juhuslik]