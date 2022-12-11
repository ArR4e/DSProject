n = int(input("Sisesta naturaalarv: "))
a = 0
b = 0

for x in range(n+1):
    a += x**2
    b += x
b *= b

print("Naturaalarvu summa ruudu ja ruutude vahe on",b-a)
