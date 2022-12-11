n = int(input("Sisestage naturaalarv: "))
i=0
rs=0
while i<=n:
    rs = rs + i**2
    i+=1
i=0
summa=0
while i<=n:
    summa = summa +i
    i+=1
sr = (summa)**2 
x = sr - rs    
print(x)