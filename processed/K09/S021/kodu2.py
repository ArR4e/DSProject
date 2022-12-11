import random
def minu_shuffle(järjend):
    for i in range(len(järjend)):
        vahetatav = random.choice(range(len(järjend)))
        järjend[i], järjend[vahetatav] = järjend[vahetatav], järjend[i]
    print(järjend)
minu_shuffle([1, 2, 3, 4])
