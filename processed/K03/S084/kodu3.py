#Küsib kasutajalt naturaalarvu
while True:
    try:
        n = int(input("Sisestage naturaalarv: "))
        break
    except:
        print("Midagi valesti")

a = n
nsum = 0
nruutsum = 0

#Liidab naturaalarvud kokku
while a > 0:
    nsum += a
    a -= 1

a = n
#Liidab naturaalarvude ruudud kokku
while a > 0:
    nruutsum += a * a
    a -= 1

#Lahutab naturaalarvude summa ruudust ruutude summa ja annab tulemuse
tulemus = nsum * nsum - nruutsum
print(tulemus)