from random import randint

def minu_shuffle(jarjend):
    for i in range(len(jarjend)):
        element = randint(0, len(jarjend)-1)
        temp = jarjend[i]
        jarjend[i] = jarjend[element]
        jarjend[element] = temp


a = [1, 3, 3, 4, 5, 5, 5, 6, 6]
print(a)
minu_shuffle(a)
print(a)