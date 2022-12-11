a=int(input("palun sisestage arv n: "))
b=a
c=1
d=1
e=1
sr=0
rs=0 
while a>0:
    rs+=c**2
    c+=1
    a-=1
while e==1 :
    while b>0:
        sr+=d
        d+=1
        b-=1
    sr=sr**2
    e-=1
erinevus=sr-rs
print("n naturaalarvu summa ruudu ja ruutude summa erinevus on " + str(erinevus))