a = int(input("Sisesta number: "))

#naturaalarvude ruutude summa
s = a * (a + 1) * (2 * a + 1) / 6

#naturaalarvude summa ruut
r = (a * (a + 1) / 2)**2

v = r - s

print("Esimese", a, "naturaalarvu summa ruudu ja ruutude summa erinevus on", int(v))