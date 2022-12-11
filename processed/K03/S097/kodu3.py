n = int(input("Sisesta naturaalarv: "))

ruutude_summa = 0
i = 0

while i <= n :
    ruutude_summa += i**2
    i += 1
    print(n, "esimese naturaalarvu ruutude summa on ", ruutude_summa)
    
summa = 0
i=0

while i <= n :
    summa += i
    i += 1
    summa_ruut=summa**2
    print(n, "esimese naturaalarvu summa ruut on ", summa_ruut)

print("Esimese", n ,"naturaalarvu summa ruudu ja ruutude summa erinevus on: ", summa**2-ruutude_summa)
