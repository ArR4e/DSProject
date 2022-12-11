from random import randint
def minu_shuffle(arvud):
    for i in range(len(arvud)):
        n = randint(0,len(arvud)-1)
        arv = arvud.pop(n)
        arvud.append(arv)
