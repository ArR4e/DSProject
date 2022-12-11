f = open("taksohinnad.txt", encoding="UTF-8")

tee_pikkus = float(input("Sisestage tee pikkus koju: "))
järjend = []
arv = 0
hind = 0

for rida in f:
    rida = rida.strip()
    järjend = rida.split(",")
    arv = float(järjend[1]) + float(järjend[2])*tee_pikkus
    if hind == 0:
        hind = arv
        nimi = järjend[0]
    elif arv < hind:
        hind = arv
        nimi = järjend[0]

try:
    print("Kõige odavam on " + nimi + ".")
except:
    print("Fail on tühi")
    
f.close()