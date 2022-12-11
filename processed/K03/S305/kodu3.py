n = int(input("Sisesta naturaalarv n: "))

m = 1
s1 = 0
s2 = 0

while m <= n:
    s1 += m**2
    m += 1

m = 1

while m <= n:
    s2 += m
    m += 1

s2 = s2**2
s = s2 - s1

print("Erinevus:", str(s))