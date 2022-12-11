n = int(input("Sisestage naturaalarv: "))
summaruut = 0
ruutudesumma = 0
i = 1
while i <= n:
    ruutudesumma += i ** 2
    summaruut += i
    i += 1

summaruut = summaruut**2
print(str(summaruut - ruutudesumma))