n = int(input("Palun sisestage naturaalarvu: "))


ruutudesumma = 1
ruut = 0
    


while ruutudesumma <= n :
    ruut += ruutudesumma**2
    ruutudesumma += 1


summaruut = 1
sum = 0

while summaruut <= n :
    sum = (summaruut + sum)
    summaruut = 1 + summaruut
print ((sum ** 2) - ruut)