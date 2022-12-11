#Ruudud
def ruutude_summa(n):
    i = 1
    summa = 0
    for i in range(n+1):
        summa += i**2
        i += 1
    return summa

def summa_ruut(n):
    i = 1
    summa = 0
    ruut = 0
    for i in range(n+1):
        summa += i
        i += 1
    ruut = summa**2
    return ruut

sisend = int(input("Sisesta üks naturaalarv: "))
print(ruutude_summa(sisend))
print(summa_ruut(sisend))