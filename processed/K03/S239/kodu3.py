n=int(input("Palun sisesta mõni naturaalarv: "))

i=1
summa1=0
while i<=n:
    summa1+=i**2
    i+=1

j=1
summa2=0
while j<=n:
    summa2+=j
    j+=1
    
vahe=summa2**2-summa1
print("Summa ruudu ja ruutude summa vahe: ",vahe)