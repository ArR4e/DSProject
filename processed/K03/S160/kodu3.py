n = int(input("Sisestage naturaalarv: "))

ruutude_summa = 0
for number in range(0, n+1):
    ruutude_summa += number**2 + number**2 
    
ruudu_summa = 0
for number in range(0, n+1):
    ruudu_summa = (number + number)**2
print(ruudu_summa- ruutude_summa)