with open("taksohinnad.txt", "r", encoding="utf-8") as f:
    hinnad = f.readlines()
    f.close()

def takso(kaugus, hinnad):
    if hinnad == []:
        return 0
    erihinnad = []
    for x in hinnad:
        erihinnad += [float(x.split(",")[1])+float(x.split(",")[2])*kaugus]
    odav = erihinnad.index(min(erihinnad))
    string = "Kõige odavam on " + str(hinnad[odav].split(",")[0])
    print(string)
kaugus = float(input("sisestage tee pikkus kilomeetrites: "))
takso(kaugus, hinnad)