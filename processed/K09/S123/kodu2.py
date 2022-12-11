from random import randint

def minu_shuffle(jär):
    for i in range(0, len(jär)):
        juh_arv=randint(0, len(jär))
        jär[i]=jär[juh_arv]