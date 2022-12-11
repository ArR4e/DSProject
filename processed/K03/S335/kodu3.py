n = int(input("Sisestage naturaalarv: "))

i = 0
tehe1 = 0
tehe2 = 0
i2 = 0
tehe3 = 0

while i <= n:
    tehe1 = i**2
    tehe2 += tehe1
    i += 1

while i2 <= n:
    tehe3 += i2
    i2 += 1

tehe3 = tehe3 ** 2
print(tehe3 - tehe2)