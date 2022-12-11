a=1
b=0
c=0
n=int(input('Mitme esimese naturaalarvu summa ruudu ja ruutude summa erinevusest oled huvitatud?'))
n=n+1
for a in range(n):
    b+=a**2
a=1
for a in range(n):
    c+=a
c=c**2-b
print(str(n)+' esimese naturaalarvu summa ruudu ja ruutude summa erinevus on '+str(c))

