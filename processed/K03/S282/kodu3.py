n=int(input("Sisestage naturaalarvude arv: "))
summaruut=0
ruudusumma=0
arv=0
for el in range(n):
    arv+=1
    summaruut+=arv
    ruudusumma+=arv**2
summaruut**=2
print(summaruut-ruudusumma)
