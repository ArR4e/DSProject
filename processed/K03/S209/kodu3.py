n = int(input("Sisesta naturaalarv: "))

summa = (n - 1)**2 + n**2 + (n+2)**2
ruut = ((n-1) + n + (n + 2))**2
vahe = summa - ruut
    
print(vahe)