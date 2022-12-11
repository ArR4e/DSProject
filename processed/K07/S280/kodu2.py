# 2. Taksohinnad / RP

fail = open("taksohinnad.txt", encoding = "UTF-8")
hinnad = []
nimed = []

pikkus = float(input("Sisesta tee pikkus kilomeetrites: "))

for rida in fail:
    uus_rida = rida.split(",")
    nimed.append(uus_rida[0])
    maksumus = float(uus_rida[1]) + float(uus_rida[2])  * pikkus
    hinnad.append(maksumus)
    
fail.close()

try:
    print("Kõige odavam on " + nimed[hinnad.index(min(hinnad))] + ".")
except:
    print("Andmed puuduvad.")