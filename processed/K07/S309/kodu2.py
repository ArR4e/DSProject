#Küsime kasutajalt distantsi
distance = float(input("Sisesta tee pikkus kilomeetrites: "))

#Avame tekstifaili mis sisaldab andmeid
taxifile = open("taksohinnad.txt", "r", encoding="UTF-8")

#Loome paar muutujat
taxi = ()
taxilist = []

#Loopime läbi faili ridade:
#Kõigepealt teeme ühe rea hästi masinloetavaks tuple-iks,
#siis lisame taksode listi kahesed listid, kus esimesel kohal on sõiduhind
#mille arvutame kasutades tuple-i väärtusi ja sisestatud distantsi,
#ning teisel kohal on taksofirma nimi
for line in taxifile:
    taxi = tuple(line.strip().split(","))
    taxilist.append([(float(taxi[1]) + float(taxi[2])*float(distance)), taxi[0]])

#Sorteerime listide listi, .sort() sorteerib listid listide esimese koha väärtuse järgi
try:
    taxilist.sort()
    #Prindime kasutajale sorteeritud listis esimesel kohal oleva listi teise koha ehk taksofirma nime
    print(f"Kõige odavam on {taxilist[0][1]}")
except Exception as e:
    print(e)

