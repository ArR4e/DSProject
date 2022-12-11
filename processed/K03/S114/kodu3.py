n = int(input("Sisesta naturaalarv: "))
m = n
a = 0 #naturaalarvu ruutude summa
x = 1
b = 0 #n naturaalarvu summa ruut
while n > 0: 
    a = a + x **2
    x +=1
    b +=n
    n -=1

print("Esimese "+str(m)+" naturaalarvu summa ruudu ja ruutude summa erinevus on "+str((b**2)-a))
    
