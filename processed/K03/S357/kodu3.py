n = int(input("Sisesta naturaalarv "))

list = range(0, (n+1))

#summa ruut
y = (sum(list))**2

#ruutude summa
x = 0
for i in range(0, (n+1)):
    x += i**2


print("Erinevus on ", y-x )