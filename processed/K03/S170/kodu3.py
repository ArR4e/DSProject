n = int(input("Palun sisestage naturaal arvuna mitme esimese ruutude summat ja summa ruutu te soovite: "))  
while n < 0:
    int(input("Palun sisestage NATURAAL arv: "))
kokku1 = 0
kokku2 = 0
while n > 0:
    l = (n)**2
    kokku1 = l + kokku1
    
    kokku2 = n + kokku2
    n = n - 1

kokku2 = (kokku2)**2
erinevus = kokku2 - kokku1

print("Ruutude summa ja summa ruudu vahe on:", str(erinevus))