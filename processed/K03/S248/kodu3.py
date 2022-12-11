n=int(input("Sisesta naturaalarv: "))

i=1 #naturaalarvud
x=0 #naturaalarvude ruutude summa
y=0 #naturaalarvude summa

while i<=n:
    x=x+i**2
    y=y+i
    i=i+1
else:
    summaruut=y**2

print(summaruut - x)