
n = int(input("sisestage täisarv: "))
a=n
fakt =  1
while n > 1:
    fakt = fakt + n
    n = n -1
ruudus = fakt**2

   
summa = 0
while a > 0:
    summa = summa + (a*a)
    a = a - 1



vahe = ruudus - summa
print(vahe)