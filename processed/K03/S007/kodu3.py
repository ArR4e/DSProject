a = int(input("Sisestage naturaalarv: "))
#x on ruutude summa
#y on summa ruut
x=0
y=0

i=a
j=a

while i>0:
    x+=i**2
    i-=1
    
while j>0:
    y+=j
    j-=1
    
y=y**2
b= y-x
print("Naturaalarvu ruudu summa ja summa ruudu erinevus on:",b)