a=int(input("Sisestage arv: "))

d=0
e=0
b=1

while a>=b:
    c=b*b
    d += c
    e += b
    b +=1

print("Esimese "+ str(a) +" naturaalarvu ruutude summa on "+str(d))
print("Esimese "+ str(a) +" naturaalarvu summa ruut on "+str(e**2))
print("Esimese "+ str(a) +" naturaalarvu summa ruudu ja ruutude summa erinevus on "+str(e**2-d))