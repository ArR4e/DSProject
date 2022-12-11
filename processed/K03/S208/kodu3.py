n = int(input("Sisesta naturaalarv: "))
ruutudesumma = 0
m = n
summaruut = 0
while n > 0 :
    ruutudesumma = ruutudesumma + (n * n)
    n = n - 1
while m > 0 :
    summaruut = summaruut + m
    m = m - 1
summaruut = summaruut ** 2
summa = summaruut - ruutudesumma
print(summa)