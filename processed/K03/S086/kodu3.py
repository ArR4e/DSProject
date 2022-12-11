#Ruudud
while True:
    try:
        arv = int(input("Palun sisesta üks naturaalarv: "))
        break
    except:
        print("Kas sisestasid ikka naturaalarvu?")

#Ruutude summa
ruutude_summa = 0
for i in range(arv):
    ruutude_summa += (i+1)**2 #i'le tuleb 1 liita, sest lugemine algab 0st

#Summaruut
summa = 0
for i in range(arv):
    summa += (i+1)
summaruut = summa**2

print("Esimese " + str(arv) + " naturaalarvu summa ruudu ja ruutude summa erinevus on " + str(summaruut - ruutude_summa))