n=int(input("Siseta n: "))
ruutudesumma=0
summa=0
while n>0:
    ruutudesumma=ruutudesumma + n**2
    summa=summa + n
    n-=1
    
summaruut=summa**2
print(str(summaruut-ruutudesumma))