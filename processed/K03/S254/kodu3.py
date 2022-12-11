#ruudud

n = abs(int(input("sisesta naturaalarv: ")))
#n=10
i=0
ruutudesumma=0
summa=0
while i<=n:
    ruutudesumma+=i**2
    summa+=i
    i+=1

summaruut=summa**2

erinevus=summaruut-ruutudesumma

print("Arvude erinevus on " + str(erinevus))