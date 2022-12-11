n = int(input("Sisesta naturaalarv: "))
def ruutude_summa(n):
    i = 0
    uus_arv = 0
    for i in range(1, n+1):
        arv = i**2
        uus_arv+=arv
        n -= 1
        i += 1
    return uus_arv
def summa_ruut(n):
    summa_arv = 0
    i = 0
    for i in range(1, n+1):
        arv = i
        summa_arv += arv
        n -= 1
        i += 1
    summa_arv = summa_arv ** 2
    return summa_arv
print(summa_ruut(n) - ruutude_summa(n))
