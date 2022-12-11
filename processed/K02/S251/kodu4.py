inglise_sisestus = input("Sisestage inglisekeelne tekstifail, mida soovite tõlkida: ")
eesti_sisestus = input("Sisestage tekstifail, kuhu tõlge saata: ")

inglise_tekst = open(inglise_sisestus,'r')
eesti_tekst = open(eesti_sisestus, 'w')

inglise_tekst = inglise_tekst.read()
asenduste_arv = inglise_tekst.count('Hello')

vahetekst = ''
c = 0

for i in range(len(inglise_tekst)):
    if i + c >= len(inglise_tekst):
        break
    if inglise_tekst[i+c:i+5+c] == 'Hello':
        c += 4
        vahetekst += 'Tere'
    else:
        vahetekst += inglise_tekst[i+c]
        
eesti_tekst.write(vahetekst)
eesti_tekst.close()

print("Tekstis tehti " + str(asenduste_arv) + " asendust.")

#loetav = open(eesti_sisestus,'r')
#print(loetav.read())
# Soovi korral saab tõlgitud tekstifaili lugeda
    