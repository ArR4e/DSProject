def minu_shuffle(järjend):
    from random import randint
    arve = len(järjend) - 1
    s = 0
    for i in järjend:
        n =  randint(0,arve)
        järjend[s], järjend[n] = järjend[n], järjend[s]
        s += 1
    print(järjend)