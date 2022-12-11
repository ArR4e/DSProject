n = int(input("Sisesta mingi positiivne naturaalarv: "))
i=0
ruutsum = 0
sumruut = 0

if n < 0:
    print("Sisesta mingi positiivne naturaalarv.")
else:
    while i <= n:
        ruutsum += i**2
        sumruut += i
        i += 1
print("Naturaalarvu summa ruudu ja ruutude summa erinevus on: "+str(sumruut**2-ruutsum)+".")