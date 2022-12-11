n = int(input("Sisesta naturaalarv: "))
a = 1
rs = 0
sr = 0

while a <= n:
    a = a ** 2
    rs += a
    a += 1
    
while a <= n:
    sr += a
    a += 1
    if a > n:
        sr = sr ** 2

vahe = sr - rs

print(sr)
print(rs)
print(vahe)