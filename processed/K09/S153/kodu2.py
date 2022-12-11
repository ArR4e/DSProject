import random

def minu_shuffle(järjend):
    järjend = [int(k) for k in järjend]
    uus_järjend = järjend.copy()
    for el in järjend:
        i = järjend.index(el)
        uus_i = random.randint(0, len(järjend))
        for n in uus_järjend:
            uus_järjend.pop(n[uus_i])
            uus_järjend.append(el[uus_i])
    return uus_järjend
