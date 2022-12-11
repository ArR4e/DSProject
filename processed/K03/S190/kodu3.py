n = int(input("Sisesta naturaalarv: "))

x = 0
summa_ruut = 0
for i in range(n):
    x += i+1
    
    summa_ruut = x**2

y = 0
ruutude_summa = 0
for i in range(n):
    y += (i+1)**2
    
    ruutude_summa = y

print(abs(summa_ruut-ruutude_summa))