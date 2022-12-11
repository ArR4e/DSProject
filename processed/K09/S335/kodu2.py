from random import choice, randint
def minu_shuffle(järjend):
    i = 0
    while i < len(järjend):
        element = [choice(järjend)]
        indeks = järjend.index(element[0])
        järjend.remove(järjend[indeks])
        järjend.insert(randint(0, len(järjend)), element[0])
        i += 1