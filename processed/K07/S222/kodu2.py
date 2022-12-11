fail = open("taksohinnad.txt","r")
sisu = []
for rida in fail:
    sisu.append(rida.strip().split(","))
fail.close()

km = float(input("Sisesta tee pikkus kilomeetrites: "))
if km > 0 and km < 1:
    km = 1
    
maksi = 2+0.6*km
sõps = 10
waldo = 1+km

odavaim = min([maksi,sõps,waldo])
if odavaim == maksi:
    print("Kõige odavam on Maksitaksi")
elif odavaim == sõps:
    print("Kõige odavam on sõbraga")
elif odavaim == waldo:
    print("Kõige odavam on Waldo takso")