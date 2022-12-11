from random import choice
def minu_shuffle(järjend):
    uus = järjend.copy()
    for el in uus:
        suvakas = choice(uus)
        järjend.append(suvakas)
        järjend.remove(suvakas)