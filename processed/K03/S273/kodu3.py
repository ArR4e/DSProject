a = 1
n = int(input("Kirjuta üks naturaalarv: "))
ruutude_summa = 0
summa = 1

while a < n:
    ruutude_summa += (a + 1) ** 2
    a += 1
    summa += a
#print((summa ** 2), " ja", ruutude_summa)
print((summa ** 2) - ruutude_summa - 1)
    
