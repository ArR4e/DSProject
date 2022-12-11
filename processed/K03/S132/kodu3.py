while True:
    try:
        n = int(input("Sisesta naturaalarv: "))
        if n < 0:
            print("See ei ole naturaalarv, proovi uuesti")
            continue
        break
    except:
        print("Sisestatu polnud number või ei olnud täisarvu kujul, proovi uuesti")

n2 = n
n3 = n
#Esimese n naturaalarvu ruutude summa:
ruutude_summa = 0
while n != 0:
    ruutude_summa += n**2
    n -= 1


#Esimese n naturaalarvude summa ruut:
summa_ruut = 0
while n2 != 0:
    summa_ruut += n2
    n2 -= 1
summa_ruut = summa_ruut ** 2

erinevus = summa_ruut - ruutude_summa

print(f"esimese {n3} naturaalarvu summa ruudu ja ruutude summa erinevus on {erinevus}.")


