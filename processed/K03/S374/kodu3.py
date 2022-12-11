n=int(input('Sisestage naturaalarv n: '))

ruutudesumma=0
summaruut=0

while n!=0:
    ruutudesumma+=pow(n, 2)
    summaruut+=n
    n-=1
    
summaruut=pow(summaruut, 2)
vahe=summaruut-ruutudesumma

print(vahe)