#kodu3 - ruudud
i = 1
ruutude_summa = 0
summa_ruut = 0
n = int(input("Sisesta naturaalarv: "))
while i <= n:
    ruutude_summa = ruutude_summa + i**2
    summa_ruut = summa_ruut+i
    i = i+1
print(str(((summa_ruut)**2-ruutude_summa)))
