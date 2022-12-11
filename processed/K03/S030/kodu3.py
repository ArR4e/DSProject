n=int(input("Sisesta naturaalarv: "))
sum=0
sum1=0
while n>0:
    sum=sum+(n**2)
    sum1=(n+sum1)
    n=n-1
vahe=sum1**2-sum
print("Ruutude summa ja summa ruudu erinevus on " + str(vahe)+ ".")