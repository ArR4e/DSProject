arv = int(input("arv: "))

def ruutude_summa(n):
    summa = 0
    for i in range(1, n+1):
        summa += i * i
    return summa

def summa_ruut(n):
    ruut = 0
    for i in range(1, n+1):
        ruut += i
    return ruut*ruut
    
print(summa_ruut(arv) - ruutude_summa(arv))
