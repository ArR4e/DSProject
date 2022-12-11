from random import *
def minu_shuffle(jada):
    if len(jada) > 1:
        for i in range(len(jada)):
            arv = randint(0, len(jada) - 1)
            jada[i], jada[arv] = jada[arv], jada[i]