n=x=float(input("Sisesta naturaalarv"))
x=int(n)

if n!= x:
    while n != x:
        
        print ("Sisesta naturaalarv, mitte murd")
        
        n=input("Sisesta naturaalarv")
        x=int(n)

s1=0
s2=0
while n!=0 :
    s1=s1+n**2
    s2=s2+n
    n=n-1
    print(s1)
    print(s2)
    
print("Esimese", x, "naturaalarvu summade ruudu ja ruutude summa erinevus on", s2**2-s1)


    