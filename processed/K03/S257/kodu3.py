n = int(input("Sisestage naturaalarv: "))

rsumma = 0
summar = 0

i = 0
while i <= n:
    i+=1
    rsumma += i**2
    summar += i
summar = summar**2
print("Arvude erinevus on", summar-rsumma)