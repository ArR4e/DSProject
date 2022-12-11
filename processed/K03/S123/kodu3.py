n=int(input("Sisesta naturaalarv: "))
i=1
summa=0
rsumma=0

while i<=n:
    summa+=i
    rsumma+=i**2
    i=i+1
summaruut=summa**2
#print(summaruut)
#print(rsumma)

print(summaruut-rsumma)
