n = int(input("Sisestage naturaalarv:"))
ruutude_summa = 0
for i in range(1, n+1):
    ruutude_summa = ruutude_summa + (i * i)
    
summa = int(n*(n+1)/2)

print("Ruutude summa erinevus on", summa*summa - ruutude_summa)