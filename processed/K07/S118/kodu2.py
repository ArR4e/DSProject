fail = open("taksohinnad.txt", "r", encoding="utf-8")

taksohinnad = fail.readlines()

fail.close()

antud_hinnad = {}

väikseim = -1
väikseima_hinnaga = ""
teekond = float(input("Sisesta tee pikkus kilomeetrites: "))

for rida in taksohinnad:
    nimi = rida.split(",")[0]
    sisseistumine = float(rida.split(",")[1])
    km_hind = float(rida.replace("\n","").split(",")[2])
    maksumus = sisseistumine + (km_hind * teekond)
    antud_hinnad[nimi] = maksumus
    if väikseim == -1 or maksumus < väikseim:
        väikseim = maksumus
        väikseima_hinnaga = nimi
        
print("Kõige odavam on", väikseima_hinnaga + ".")
