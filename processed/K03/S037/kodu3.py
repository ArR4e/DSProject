n = int(input("Sisestage naturaalaarv: "))
a = 0
b = 0

while n > 0:
    a += n
    b += n ** 2
    n -= 1
    
summa_ruut = a ** 2
    
ruutude_summa = b

vahe = summa_ruut - ruutude_summa

print("Esimese n naturaalarvu summa ruudu ja ruutude summa erinevus on: ", vahe)