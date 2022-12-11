n = int(input("Sisesta naturaalarv: "))
ruutude_summa  = 0
for s in range (1, n+1):
    ruutude_summa += (s*s)


summaruut = 0
for i in range (1, n+1):
    summaruut +=i
    i + 1
summaruut = summaruut**2

print (str(summaruut - ruutude_summa))