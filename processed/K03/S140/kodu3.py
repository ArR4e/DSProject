while True:
    try:
        n = int(input("Sisestage naturaalarv: "))
        if n > 0:
            break
        else:
            print("Tegemist ei ole naturaalarvuga!")
    except:
        print("Tegemist ei ole naturaalarvuga!")

a = 1
ruutudesumma = 0

b = 1
summa = 0

while a <= n:
    ruutudesumma += a**2
    a += 1

while b <= n:
    summa += b
    b += 1
summaruut = summa**2

erinevus = summaruut - ruutudesumma

print(str(n) + " naturaalarvu summa ruudu ja ruutude summa erinevus on: " + str(erinevus))
