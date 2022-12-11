naturaalarv = int(input("Sisesta naturaalarv: "))

ruut_summa = 0
n = 1
while n <= naturaalarv:
    ruut_summa = ruut_summa + n**2
    n = n + 1

arv_summa = 0
m = 1
while m <= naturaalarv:
    arv_summa = arv_summa + m
    m = m + 1

vahe = arv_summa**2 - ruut_summa

print(vahe)