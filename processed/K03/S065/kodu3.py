n = int(input("Sisesta n väärtus: "))
x = n
i = 0
b = 0
c = 0
z = 0
y = 0
k = n
for a in range(n):
    b += i # b = b + i
    n -= 1 # n = n - 1
    i = n**2 
c = x**2 + b
print(c)

for d in range(x):
    z += x
    x -= 1
y = z**2
print(y)
erinevus = y - c
print("Esimese", str(k) + "-ne naturaalarvu summa ruudu ja ruutude summa erinevus on", erinevus)