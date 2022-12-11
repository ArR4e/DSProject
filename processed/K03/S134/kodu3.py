m = int(input("Sisesta naturaalarv: "))
n = 0
i = 0
summa = 0
summaruut = 0
s = 0
while n < m:
    n += 1
    summa += n**2
while i <= m:
    s += i
    i += 1
summaruut = s**2
erinevus = summaruut - summa
print(summaruut)
print(erinevus)