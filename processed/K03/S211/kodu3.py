n = int(input("Sisesta naturaalarv: "))

i = 1
ruut = 0
ruutudesumma = 0
summaruut = 0

while i<=n:
    
    ruut = i**2
    i += 1
    ruutudesumma += ruut

  
j = 0
summaruut1 = 0
summaruut2 = 0

while j<=n:
    
    summaruut1 = j
    j += 1
    summaruut2 += summaruut1

print(summaruut2**2-ruutudesumma)