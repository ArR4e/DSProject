n=int(input('Sisesta naturaalarv: '))

i=summa1=summa2=0

while i<n:
    i+=1
    summa1+=i**2
    summa2+=i
    
print(summa2**2-summa1)