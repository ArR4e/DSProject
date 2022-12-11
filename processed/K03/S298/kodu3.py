n = int(input("Palun sisestage arv: "))
c = 1
summa1 = 0
vahes = 0
while c <= n:
    summa1 += c**2
    vahes += c
    print(c)
    c += 1
vastus = vahes**2 - summa1
print(vastus)