from random import sample
def minu_shuffle(list):
    pikkus=len(list)
    uus=sample(list, pikkus)
    list.clear()
    list.extend(uus)
    