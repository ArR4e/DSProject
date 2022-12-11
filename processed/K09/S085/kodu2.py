from random import randint
def minu_shuffle(järjend):
    for el in järjend:
        i = len(järjend) - 1
        juhuslik1 = randint(0, i)
        juhuslik2 = randint(0,i)
        järjend[juhuslik1], järjend[juhuslik2] = järjend[juhuslik2], järjend[juhuslik1]
    
