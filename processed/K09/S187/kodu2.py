from random import randint

def minu_shuffle(hulk):
    a = []
    for i in range(len(hulk)):
        asi = hulk.pop(randint(0, len(hulk) - 1))
        a.append(asi)
    hulk = a

# kontrollisin, listi a lisatakse ilusti elemente, ma tõesti ei tea, miks muutuja hulk lõpus tühi on