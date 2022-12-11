n=int(input("Sisesta naturaalarv N ja arvutan sulle nende esimeste naturaalarvude ruutude summa ja summa ruudu erinevuse:        "))
arvud=range(1,n+1)
summaruut=sum(arvud)**2
ruutudesumma=sum(i**2 for i in arvud)
vastus=abs(ruutudesumma-summaruut)
print(vastus)      