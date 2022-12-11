from random import randint 
def minu_shuffle(järjend):
    for element in järjend:
        juhuslik_indeks1 = randint(0, len(järjend)-1)
        juhuslik_indeks2 = randint(0, len(järjend)-1)
        järjend[juhuslik_indeks1], järjend[juhuslik_indeks2] = \
        järjend[juhuslik_indeks2], järjend[juhuslik_indeks1]


        