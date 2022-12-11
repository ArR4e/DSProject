n=int(input("Sisesta naturaalarv: "))
i=1
summa1=0
summa2=0
while i<=n:
    summa1=summa1+i**2
    i+=1
i=1    
while i<=n:
    summa2=summa2+i
    i+=1
summa2=summa2**2
erinevus=summa2-summa1
print(str(erinevus))