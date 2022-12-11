from random import randint

def minu_shuffle(jarjend):
    pikkus = len(jarjend)
    uus_jarjend = []
    for i in range(0, pikkus):
        uus_jarjend.append(jarjend.pop(randint(0, pikkus-i-1)))
    jarjend += uus_jarjend

a = [1, 3, 3, 4, 5, 5, 5, 6, 6]

minu_shuffle(a)
print(a)