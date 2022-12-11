n=int(input("Sisestage naturaalarv "))
sr=0
rs=0

for n in range(n+1):
    rs+=n**2
    sr+=n
    n+=1
sr=sr**2
erinevus=sr-rs

print("Selle naturaalarvu summa ruudu ja ruutude summa erinevus on ",sr-rs )