b = 0
c = 0
ruudusumma = 0
summa = 0


a = int(input("Sisestage naturaalarv"))


while b < a:
    b+=1
    summa = summa + b**2
    ruudusumma = ruudusumma + b

ruudusumma = ruudusumma**2
print("Vastus on", ruudusumma, "-", summa, "=", ruudusumma - summa)
