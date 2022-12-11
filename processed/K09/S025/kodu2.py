from random import randint

def minu_shuffle(jär):
    i = 0
    for i in range(len(jär)):
        juhuslik1 = randint(0, (len(jär)-1))
        juhuslik2 = randint(0, (len(jär)-1))
        jär[juhuslik1], jär[juhuslik2] = jär[juhuslik2], jär[juhuslik1]
        i += 1