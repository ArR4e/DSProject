n = int(input("Sisesta naturaalarv: "))
tulemus = 0
tulemus2 = 0
i = (n - n + 1) ** 2
while i <= n:
    tulemus += (i) ** 2
    i += 1
#print(tulemus)
i = (n - n + 1) ** 2
while i <= n:
    tulemus2 += i
    i += 1
tulemus2 = tulemus2 ** 2
#print(tulemus2)
print(tulemus2 - tulemus)
    