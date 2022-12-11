from random import sample
def minu_shuffle(jär):
    jär[:] = sample(jär, len(jär))
