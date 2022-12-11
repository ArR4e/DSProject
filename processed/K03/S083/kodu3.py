n = int(input('Sisestage naturaalarv n: '))
i = 1
ruutude_summa = 0
summa = 0
while i <= n:
    summa += i
    ruutude_summa = ruutude_summa + (i*i)
    i += 1
print(n, 'esimese naturaalarvu summa ruudu ja ruutude summa vahe on', \
      summa**2 - ruutude_summa,'!')
    