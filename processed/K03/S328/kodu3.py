n = int(input("Naturaalarv: "))
ruudu_summa = 0
naturaalarvu_summa = 0

for i in range(n + 1):
    ruudu_summa += i**2
    naturaalarvu_summa += i
print(naturaalarvu_summa**2 - ruudu_summa)
    