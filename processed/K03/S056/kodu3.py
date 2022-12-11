n = int(input("Sisesta naturaalarv: "))
i = 1
summa = 0
summa_2 = 0

while i <= n:
    m = (i * i)
    i += 1
    summa += m

for i in range(int(n)+1):
    summa_2 += i
    i += 1
    final = summa_2**2

vastus = final - summa
print(f"Esimese {n} naturaalarvu summa ruudu ja ruutude summa erinevus on {vastus}")