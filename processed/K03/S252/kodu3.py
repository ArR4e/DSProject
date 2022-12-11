n = int(input("Siseta naturaalarv:"))
summa = 0
ruutudeSumma = 0

for n in range (1, n+1):
    summa = summa + n
    ruutudeSumma = ruutudeSumma + (n * n)

summaRuut = summa*summa
vahe = summaRuut-ruutudeSumma

print("summa ruut: "+ str(summaRuut))
print("ruutude summa: "+ str(ruutudeSumma))
print("VASTUS => vahe: "+ str(vahe))
            





    
