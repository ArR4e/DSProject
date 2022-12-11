naturaalarv=int(input("Palun sisestage naturaalarv: "))
ruutudesumma=0
summa=0

for i in range(1, naturaalarv+1):
    ruutudesumma+=i*i
    summa+=i
    
summaruut=summa**2
vahe=summaruut-ruutudesumma
print(vahe)