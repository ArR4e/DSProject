n=int(input("Sisesta naturaalarv: "))
summa=0
ruudud=0
i=0
while i <= n:
    ruudud += i**2
    summa += i
    i += 1
a=summa**2
print("Esimese "+str(n)+" naturaalarvu summa ruudu ja ruutude summa erinevus on "+str(a-ruudud)+".")