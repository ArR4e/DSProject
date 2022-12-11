arv = int(input("sisestage positiivne naturaalarv "))
i = 1
arv2 = 0
arv3 = 0

while i <= arv:
    arv2 = arv2 + i**2
    arv3 = (arv3 + i)
    i += 1
    
arv3 = arv3**2    
print("Esimese valitud naturaalarvu summa ruudu ja ruutude summa erinevus on", abs(arv2 - arv3))
    
