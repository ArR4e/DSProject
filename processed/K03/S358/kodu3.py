#kodu3.py

arv = int(input("Sisesta arv: "))

ruut = 0
summa = 0
i = 1
while i <= arv:
    ruut += i*i
    i += 1
i = 0
while i <= arv:
    summa += i
    i += 1
summa = summa ** 2
print(abs(ruut-summa))