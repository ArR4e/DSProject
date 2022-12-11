n = int(input("Sisestage naturaalarv: "))
i = 1
e = 0
u = 0
while i <= n:
    e += i
    u += i**2
    i = i+1
    
    
summaruut = e**2
ruutudesumma = u


print("summa ruudu ja ruutude summa erinevus on: ", summaruut - ruutudesumma, "!")
