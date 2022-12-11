from random import randint

def minu_shuffle(järjend):
    for indeks in range(len(järjend)):
        juhuslik_indeks = randint(0, indeks)
        if indeks == juhuslik_indeks:
            continue
        järjend[indeks], järjend[juhuslik_indeks] = järjend[juhuslik_indeks], järjend[indeks]
#    print(järjend)
        
#minu_shuffle([1, 3, 3, 4, 5, 5, 5, 6, 6])