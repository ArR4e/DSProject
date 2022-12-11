from random import randint

järjend = [1, 3, 3, 4, 5, 5, 5, 6, 6]

def minu_shuffle(järjend):
    uus_järjend = []
    kasutatud_indeks = []
    for i in range(0, len(järjend)):
        juhuslik_arv = randint(0, len(järjend)-1)
        if not juhuslik_arv in kasutatud_indeks:
            suvaliige = järjend[juhuslik_arv]
            uus_järjend = uus_järjend + [suvaliige]
            kasutatud_indeks = kasutatud_indeks + [juhuslik_arv]
        else:
            continue
    järjend = uus_järjend
            
    return järjend
print(minu_shuffle(järjend))