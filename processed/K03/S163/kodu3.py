n = int(input('Sisesta naturaalarv n: '))
ruutude_summa = 0
summa = 0
i = 1

while i <= n:
    ruutude_summa += i**2
    summa += i
    i += 1
    
erinevus = summa ** 2 - ruutude_summa

print('Esimese n naturaalarvu summa ruudu ja ruutude summa erinevus on ' + str(erinevus) + '.')
    
    