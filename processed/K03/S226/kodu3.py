#input data
b = 0
n = int(input("Palun sisestage naturaalarv: "))
# Ruutude summa
for code in range (1, n + 1):
    a = code**2
    b = b + a

#naturaalarvu summa
i = 1
summa = 0
while i <= n:
    summa += i
    i  += 1

#naturaalarvu summa ruudu
ruutsumma = summa ** 2

#erinevus 
finalstep = ruutsumma - b

#valjastamine
print(f"Seega esimese {n}. naturaalarvu summa ruudu ja ruutude summa erinevus on {ruutsumma} - {b} = {finalstep}")