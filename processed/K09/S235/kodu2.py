from random import randint

def minu_shuffle(järjend):
    for i in järjend:
        a = järjend.index(i)
        b = randint(0, len(järjend)-1)
        järjend[a] = järjend[b]
        järjend[b] = i
    print(järjend)