from random import randint
järjend = [1, 3, 3, 4, 5, 5, 5, 6, 6]

def minu_shuffle(järjend):
    i = 0
    for el in järjend:
        pop = järjend.pop(i)
        suvaline = järjend.insert(randint(0, len(järjend)), pop)
        i += 1
