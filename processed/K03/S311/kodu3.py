x = int(input("Sisesta naturaalarvude kogus n: "))
i = 1
a = 0
while i <= x:
    a += i**2
    i = i + 1
o = 1
e = 0
while o <= x:
    e += o
    o = o + 1
heh = (e**2)-a
print("Esimese n naturaalarvu summa ruudu ja ruutude summa erinevus on ", heh)