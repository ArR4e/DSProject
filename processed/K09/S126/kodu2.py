a = [1, 3, 3, 4, 5, 5, 5, 6, 6]

from random import randint
def minu_shuffle(järjend):
    for element in järjend:
        x = järjend.pop()
        asukoht = randint(0, len(järjend))
        järjend.insert(asukoht, x)
    print(järjend)
    
minu_shuffle(a)