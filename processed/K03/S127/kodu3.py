n=int(input("Sisesta naturaalarv: "))
summa=0
i=0
while i<=n:
    summa +=i
    i+=1
summa_ruut=summa*summa
ruudud=1
for i in range(2, n+1):
    ruudud+=i**2
print(summa_ruut-ruudud)
