n = int(input("Sisesta suvaline naturaalarv: "))

rsumma = 0
summar = 0
i = 0
while i <= n:
    rsumma += i**2
    summar += i
    i += 1
summar = summar**2
print(str(n) + " esimese naturaalarvu summa ruudu ja nende arvude ruutude summa erinevus on " + str(summar - rsumma))