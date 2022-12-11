n = int(input('Sisesta mitme liikme summa leitakse: '))
#mis leiab esimese n naturaalarvu summa ruudu ja ruutude summa erinevuse.

summa_ruut = 0
ruutude_summa = 0
while n > 0:
    if summa_ruut == 0:
        summa_ruut = n*n
        summa = n + (n - 1)
        ruutude_summa = summa * summa
        n -= 1
    else:
        summa_ruut = summa_ruut + (n*n)
        n -= 1
        summa = summa + n
        ruutude_summa = summa * summa
erinevus = ruutude_summa - summa_ruut      
print(erinevus)