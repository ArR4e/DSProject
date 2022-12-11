pikkus = int(input("Sisestage liinipikkus: "))
kaugus = int(input("Sisestage kõrvutiasetsevate postide maksimaalkaugust: "))

a = pikkus/kaugus
if a == int(a):
    n = a + 1
else:
    n = int(a) + 2
print(n)