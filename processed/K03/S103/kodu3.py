n = int(input("Sisesta naturaalarv n: "))

def ruutude_summa(arv):
    i = 1
    summa = 0
    while i <= arv:
        summa += i**2
        i += 1
    return summa


def summa_ruut(arv):
    i = 1
    summa = 0
    while i <= arv:
        summa += i
        i += 1
    return summa**2

erinevus = summa_ruut(n) - ruutude_summa(n)
print(erinevus)
