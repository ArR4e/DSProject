from random import randint
def minu_shuffle(jarjend):
    uus_jarjend = []
    pikkus = len(jarjend)
    n = 0
    for i in jarjend:
        randomnum = randint(0, pikkus)
        jarjend.pop(n)
        n += 1
        jarjend.insert(randomnum, i)
    print(jarjend)
minu_shuffle([100])