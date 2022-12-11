from random import*
def minu_shuffle(järjend):
    järjendi_pikkus = len(järjend)
    for indeks in range(järjendi_pikkus):
        uus_indeks = randint(0, järjendi_pikkus - 1)
        järjend[indeks] = järjend[uus_indeks]
    print(järjend)
    

minu_shuffle([2, 1, 3, 16])