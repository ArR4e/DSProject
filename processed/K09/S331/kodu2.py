from random import randint
def minu_shuffle(järjend):
    for i in range(len(järjend)):
        juhuslik_indeks = randint(0,i)
        if juhuslik_indeks == i:
            continue
        järjend[i], järjend[juhuslik_indeks] = järjend[juhuslik_indeks], järjend[i]
    

