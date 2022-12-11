from random import randint

def minu_shuffle(jada):
    for i in range(len(jada) -1, 0, -1): #src: https://www.geeksforgeeks.org/python-ways-to-shuffle-a-list/
        m = randint(0, i)
        jada[i], jada[m] = jada[m], jada[i]
