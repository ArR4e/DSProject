n = int(input("Sisestage naturaalarv: "))
summaRuut = 0
ruutudeSumma = 0
for prgArv in range(n):
    summaRuut += prgArv + 1
    ruutudeSumma += (prgArv+1)**2
summaRuut = summaRuut**2
arvudeVahe = summaRuut - ruutudeSumma
print(arvudeVahe)