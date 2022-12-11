n = int(input("Sisesta naturaalarv: "))

#esimese n arvu summa ruut?
#esimese n arvu ruutude summa?
#erinevus?

summa = 0
i = 0

while i <= n :
    summa += 1
    i += 1
summa_ruut = summa * summa

summaj = 0
j = 0

while j <= n :
    ruut = j * j
    summaj += ruut
    j += 1
    
tulemus = summa_ruut - summaj

print( n, "Nende summa ruudu ja ruutude summa einevus on: ", tulemus)
    