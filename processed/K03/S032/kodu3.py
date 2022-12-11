n = int(input("Sisesta naturaalarv n = ")) #n naturaalarvu

i=1
ruutude_summa = 0
summa = 0
while i<=n:
    ruutude_summa += i**2
    summa += i
    i+=1
    

print("Vahe on", summa**2-ruutude_summa)