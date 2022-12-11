n = int(input( " Sisesta naturaalarv: "))
summa = 0
i = 1
if n <= 1:
    print( " Tegemist pole naturaalarvuga " )
while i <= n:
    summa += i*i
    i += 1
summa1 = 0
i = 1
while i <= n:
    summa1 += i
    i += 1
summa2 = summa1**2
vahe = summa2 - summa
print( " Summa ruudu ja ruutude summa erinevus on",vahe)
    