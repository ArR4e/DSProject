# Taksohinnad

f = open("taksohinnad.txt", encoding="UTF-8")

tee_pikkus = float(input("Sisestage tee pikkus kilomeetrites: "))

hinnad = []
taksod = []

# tsükkel, mis käib läbi faili kõik read
for rida in f:
    # lisan loetud rea listi ja eraldan koma juurest
    andmed = rida.strip().split(",")
    # lisan takso nime ja hinna uutesse järjenditesse
    taksod.append(andmed[0])
    hinnad.append(float(andmed[1]) + float(andmed[2]) * tee_pikkus)

f.close()
if len(hinnad) == 0 and len(taksod) == 0:
    print("Fail on tühi!")
else:
    print("Kõige odavam on: " + taksod[hinnad.index(min(hinnad))])