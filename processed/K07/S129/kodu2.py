#Taksohinnad

sisend = float(input("Sisesta kilomeetrite arv: "))

taksolist = {}
with open("taksohinnad.txt", encoding="UTF-8") as f:
    for el in f:
        jupid = el.split(",")
        nimi = jupid[0]
        alustushind = float(jupid[1])
        kmhind = float(jupid[2])
        koguhind  = alustushind + kmhind*sisend
        taksolist[nimi] = koguhind

if sisend != 0 and sisend > 0:
    print(f"Odavaim on {min(taksolist, key=taksolist.get)}")
else:
    print("Sisesta sobilik kilomeetrite arv")









