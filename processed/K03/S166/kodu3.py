a = int(input("Sisesta naturaalarv: "))
i = 1
m = 0
n = 0
if a<0:
    print("Ma ütlesin, et sisesta NATURAALARV -.-")
else:
    while i<=a:
        m = m + (i**2)
        n = n + i
        i = i + 1
    n = n**2
    
    print("Arvude summa ruudu ja arvude ruutude summa vahe on ", n-m)