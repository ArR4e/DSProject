tee_pikkus = float(input("Sisesta tee pikkus kilomeetrites: "))

f = open("taksohinnad.txt", encoding="UTF-8")
maksitaksi = []
sõps_veab = []
Waldo_takso = []

for rida in f:
    maksitaksi = rida.strip().split(",")
    rida2 = f.readline().strip()
    sõps_veab = rida2.strip().split(",")
    rida3 = f.readline().strip()
    waldo_takso = rida3.strip().split(",")

#hind = stardihind + tee_pikkus*kilomeetri_tasu
hind1 = float(maksitaksi[1]) + float(maksitaksi[2])*tee_pikkus
hind2 = float(sõps_veab[1])
hind3 = float(waldo_takso[1]) + float(waldo_takso[2])*tee_pikkus

if hind1 > hind3 and hind2 > hind3:
    print("Kõige odavam on Waldo takso.")
elif hind1 > hind2 and hind3 > hind2:
    print("Kõige odavam on Sõps veab.")
elif hind2 > hind1 and hind3 > hind1:
    print("Kõige odavam on Maksitaksi.")
    
f.close()