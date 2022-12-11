import random

def minu_shuffle(jär):
    for i in jär:
        suvaline_nr = random.randint(0, len(jär)-1)
        jär[jär.index(i)], jär[suvaline_nr] = jär[suvaline_nr], jär[jär.index(i)]