# Ülesanne 2 minu_shuffle (kodutöö 9.nädal)

from random import randint

def minu_shuffle(järjend):
    if järjend != []:
        for i in range(len(järjend)):
            alg = randint(0, len(järjend)-1)
            arv1 = järjend[alg]
            lõpp = randint(0, len(järjend)-1)
            arv2 = järjend[lõpp]
            
            if alg == lõpp:
                continue
            else:
                järjend[alg] = arv2
                järjend[lõpp] = arv1