from random import randint
a = [1, 3, 3, 4, 5, 5, 5, 6, 6]
def minu_shuffle(jarjend):
    n = 0
    for el in jarjend:
        jarjend.insert(randint(0, len(jarjend)-1), jarjend.pop(randint(0, len(jarjend)-1)))
        n += 1
