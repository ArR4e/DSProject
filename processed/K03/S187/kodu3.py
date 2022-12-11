n = int(input("Tahaks juba magama minna, ole hea ja aita mul see progeülesanne ära teha. Sisesta mingi arv: "))

summa = 0
ruutude_summa = 0
for i in range(0, n + 1):
    summa += i
    ruutude_summa += i**2

print("See asi, mida taheti on", summa**2 - ruutude_summa)