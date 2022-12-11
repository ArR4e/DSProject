n = int(input("Sisesta arv: "))

summa = 0
i = 0

while i <= n:
      summa += i ** 2
      i += 1
      
print("Esimese ", n, "naturaalarvu ruutude summa on ", summa)

summax = 0
ix = 0

while ix <= n:
      summax += ix
      ix += 1
loppsum = summax ** 2
print("Esimese ", n, "naturaalarvu summa ruut on ", loppsum)
print()
print("Naturaalarvude summa ruudu ja ruutude summa vahe on ", loppsum - summa)