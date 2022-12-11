n = int(input("Sisestage naturaalarv: "))

i = 1
ruutudesumma = 0
summaruut = 0

while i<=n:
    ruutudesumma += i**2
    summaruut += i
    i += 1
summaruut **= 2
print(summaruut - ruutudesumma)