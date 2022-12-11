arv = int(input("Sisestage naturaalarv: "))
a = 1
b = 1
summa = 0
while a <= arv :
    b = a**2
    summa +=b
    a+=1

x = 1
y = 1
sumka = 0
while x<=arv :
    sumka=sumka+x
    x=x+1
sumka=sumka**2
print(sumka-summa)