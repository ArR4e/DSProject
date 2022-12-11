i=1
summa=0
astme_summa=0
arv = int(input("Sisesta täisarv :"))

while i<= arv:
    summa += i
    astme_summa += i**2
    i += 1

lahendus = (summa**2) - astme_summa
print(lahendus)
    