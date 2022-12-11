n = int(input("Sisestage naturaalarv: "))

i = 1
ruutude_summa = 0
summa_ruut = 0

if n <= 0:
    print("See ei ole naturaalarv")
    
else:
    while i <= n:
        ruutude_summa += i**2
        summa_ruut += i
        i += 1
        
    erinevus = summa_ruut**2 - ruutude_summa
    
    print("Summa ruudu ja ruutude summa erinevus on ", str(erinevus))
