n = int(input("Sisesta naturaalarv n: "))

a = n
b = 0
c = 0

for i in range(n):
    a -= 1
    b += a**2
ruutude_summa = n**2 + b

for i in range(n):
    a += 1
    c += a
summa_ruut = c**2

erinevus = summa_ruut - ruutude_summa

print("Esimese", str(n) + "-ne naturaalarvu summa ruudu ja ruutude summa erinevus on", str(erinevus) + ".")