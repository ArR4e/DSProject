n = int(input("Sisestage mingi naturaalarv: "))
ruutude_summa = 0
summa = 0
i = 1
while i < n+1:
    ruutude_summa = ruutude_summa + i**2
    summa = summa + i
    i += 1
    
print(summa**2 - ruutude_summa)
