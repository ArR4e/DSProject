import random

def minu_shuffle(järjend):
    tulemus = []
    while len(järjend) > 0:
        index = random.randrange(0, len(järjend))
        tulemus.append(järjend.pop(index))
    return tulemus

a = [1,2,3,4,5]
print(minu_shuffle(a)) 