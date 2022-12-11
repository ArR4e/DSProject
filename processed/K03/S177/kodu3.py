n=int(input("Sisestage naturaal arv: "))
summa1=0
for s in range (1, n+1):
    summa1 = summa1 + (s*s)
summa2=0
for r in range (1, n+1):
    summa2=summa2+r
summar = ((summa2)**2)
print ("Vastus on ", summar-summa1)
