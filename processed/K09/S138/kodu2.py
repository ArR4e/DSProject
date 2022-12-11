from random import randint
def minu_shuffle(arvud):
    x = len(arvud)
    for i in range(x):
        rand = randint(i,x-1)
        arvud[i], arvud[rand] = arvud[rand], arvud[i]