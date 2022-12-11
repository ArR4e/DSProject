n = int(input("Palun sisestage naturaalarv: "))
i=1
summa=0
ruudusumma=0
while i<=n:
    summa+=i
    ruudusumma= ruudusumma+ i**2
    i+=1
summaruut= summa**2
print("Teie valitud esimese n naturaalarvu summa ruudu ja ruutude summa vahe on:", summaruut - ruudusumma)
