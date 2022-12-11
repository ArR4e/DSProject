from random import randint

def minu_shuffle(listi):
    for i in range(0, len(listi)):
        if len(listi) == 1:
            break
        else:
            j = randint(0, i)
            listi[i], listi[j] = listi[j], listi[i]