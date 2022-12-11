from random import*

def minu_shuffle(järjend):
    i = 0
    while i < len(järjend):
        arv = randint(0, len(järjend)-1)
        a = järjend.pop(arv)
        järjend.append(a)
        i += 1


        