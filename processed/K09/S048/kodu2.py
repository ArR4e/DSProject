from random import randint

def minu_shuffle(järjend):
    if järjend !=[]:
        for i in range(len(järjend)):
            alg_indeks = randint(0, len(järjend) - 1)
            alg_arv = järjend[alg_indeks]
            lõpp_indeks = randint(0, len(järjend)- 1)
            lõpp_arv = järjend[lõpp_indeks]
            if alg_indeks == lõpp_indeks:
                continue
            else:
                järjend[alg_indeks] = lõpp_arv
                järjend[lõpp_indeks] = alg_arv