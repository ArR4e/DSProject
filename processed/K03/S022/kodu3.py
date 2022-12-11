naturaalarv = -1
while naturaalarv < 0:
    naturaalarv = int(input("Sisesta naturaalarv: "))
    
# ruutude summa
summaruut = 1
summapluss = 1
ruutudesumma = 0
while summapluss <= naturaalarv:
    summaruut = summapluss**2
    ruutudesumma = ruutudesumma + summaruut
    summapluss = summapluss + 1
#print(rsumma)
    
#summaruut
rpluss = 1
summaruut = 0
while rpluss <= naturaalarv:
    summaruut = summaruut + rpluss
    rpluss = rpluss + 1

summaruut = summaruut**2
vahe = summaruut - ruutudesumma
print(vahe)
    
#summaruut