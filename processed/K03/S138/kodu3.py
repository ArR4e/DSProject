n = int(input("Positiivne arv:"))
i = 0
sum1 = 0
sum2 = 0
if n < 0:
    print("Sisestage positiivne arv.")
while i <= n:
    sum1 = sum1 + i**2
    sum2 = sum2 + i
    i = i + 1
sum2 = sum2**2
sum = sum2- sum1

print("Esimese "+str(n)+" naturaalarvude summa ruudu ja ruudu summa erinevus on "+str(sum)+".")
    
    
