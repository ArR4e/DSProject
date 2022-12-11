from random import randint
def minu_shuffle(järjend):
    suurim_indeks = len(järjend)
    for i in range(suurim_indeks):
        carry = järjend[i]
        random_el = randint(0,suurim_indeks-1)
        võetud_el = järjend[random_el]
        järjend[random_el] = carry
        järjend[i] = võetud_el