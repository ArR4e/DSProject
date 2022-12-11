a = float(input("Sisestage tee pikkus kilomeetrites: "))

f = open("taksohinnad.txt", encoding = "UTF-8")
hinnad = []
nimed = []

for i in f:
    i = i.strip().split(',')
    nimed.append(i[0])
    hind = float(i[1]) + a * float(i[2])
    hinnad.append(hind)
if hinnad != []:
    p = hinnad.index(min(hinnad))
    print("Kõige odavam on " + nimed[p])
else:
    print("Tekstifailis puuduvad vastavad andmed.")
f.close()