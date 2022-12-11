n = int(input("Sisesta naturaalarv: "))
summa = 0
ruutude_summa = 0
i = 0
while i <= n:
    summa += i
    ruutude_summa += i*i
    i += 1
print(f"Esimese {n} naturaalarvu summa ruudu ja ruutude summa vahe on {summa**2 - ruutude_summa}")

#Ma tegin summa ruutu tõstmise ja lahutustehte lõpus print käsu sees

    