n=int(input("sisesta naturaalarv: "))
a=0
b=0
summa=0
summaruut=0
ruutudesumma=0
while a<=n:
    summa+=a
    a+=1
    summaruut=summa**2
    
while b<=n:
    ruutudesumma+=b**2
    b+=1
    
print(abs(summaruut-ruutudesumma))