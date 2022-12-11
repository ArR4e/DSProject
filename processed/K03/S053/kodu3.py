n = int(input("Sisestage arv: "))

ruutude_summa = 0
i = 0

while i <= n:
    ruutude_summa += i**2
    i += 1
    
summade_ruut = 0
j = 0
while j<= n:
    summade_ruut += j
    j += 1

print(summade_ruut**2 - ruutude_summa)

