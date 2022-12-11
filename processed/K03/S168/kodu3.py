while True:
    try:
        n = int(input("Sisesta naturaalarv n: "))
        if n < 0:
            raise Exception
        break
    except:
        print("Sisesta uuesti.")
summa1 = 0
i = 1
while i <= n:
    summa1 += i * i
    i = i + 1
i = 1
summa2 = 0
while i <= n:
    summa2 += i
    i = i + 1
summa2 = summa2 ** 2
print("Naturaalarvu summa ruudu ja ruutude summa erinevus on", summa2 - summa1)