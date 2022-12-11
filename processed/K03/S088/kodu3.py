#counterid
i = 1
x = 0
#ruutude summa ja summa ruudu alg väärtused
ruut = 0
summ = 0

a = input("Sisestage naturaalarv: ")

#Küsitakse uut sisendit nii kaua kuni see on naturaal arv
while(True):    
    if a.isdigit(): ## isdigit() aksepteerib ainult araabia numbreid
        a = int(a)
        break
    else:
        a = input("Sisestage naturaalarv: ")

#a naturaalarvude ruutude summa
while i <= a:
    s = i ** 2
    i += 1
    ruut += s

#a naturaalarvude summa ruudus
while x <= a:
    summ += x
    x += 1
summ **= 2

print(summ - ruut)