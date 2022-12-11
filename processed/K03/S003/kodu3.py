naturaalarv = int(input("Palun sisesta naturaalarv: "))

i = 1
ruutudesumma = 0
summaruut = 0

while i <= naturaalarv:
    ruutudesumma = ruutudesumma + i**2
    summaruut = summaruut + i
    i = i + 1

summaruut = summaruut**2

print(summaruut - ruutudesumma)