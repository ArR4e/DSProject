arv = int(input("Sisesta naturaalarv: "))
a=arv
i=0
summa1 = 0
summa2 = 0
while i<=a:
    summa1 += arv*arv
    summa2 += (arv)
    arv-=1
    i+=1
erinevus = summa2*summa2-summa1
print("Erinevus on:",erinevus)