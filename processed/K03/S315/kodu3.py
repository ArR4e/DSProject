a = int(input("Ütle üks kuradi suur naturaalarv "))
b = 0 #ruutude summa
c = 1
i = 0

while i != a:
    b += (a - (a - c))**2
    c += 1
    i += 1

s = 0 #summa ruut
y = 1
x = 0

while x != a:
    s += a - (a - y)
    y += 1
    x += 1
    
s = s ** 2

print(s - b)