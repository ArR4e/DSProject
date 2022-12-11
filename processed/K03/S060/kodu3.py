sisend = int(input("Sisestaga soovitud arv:"))
sisend2 = sisend
esumma=0
tsumma=0
while sisend > 0:
    esumma = esumma+sisend**2
    sisend=sisend-1
while sisend2 > 0:
    tsumma=tsumma+sisend2
    sisend2=sisend2-1
tsumma=tsumma**2
vastus=tsumma-esumma
vastus=str(vastus)
print(vastus)