naturaal_arv = int(input("Sisestage naturaalarv: "))
i = 1
ruutude_summa = 0
summa_ruut = 0
while i <= naturaal_arv:
   ruutude_summa = ruutude_summa + (i*i)
   summa_ruut+=i
   i += 1
summa_ruut = pow(summa_ruut,2)
print(summa_ruut-ruutude_summa)
    