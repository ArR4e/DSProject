natarv = int(input("Sisesta naturaalarv: "))

a = 1
natsumma = 0
summaruut = 0

 #naturaalarvu ruutude summa
while a <= natarv:
    
    m = a**2
    natsumma += m
    summaruut += a
    a += 1
    
summaruut = summaruut**2

vahe = summaruut - natsumma

print(vahe)