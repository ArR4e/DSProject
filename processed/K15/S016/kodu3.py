sisend = input("sisesta failinimi: ")
f = open(sisend, "r", encoding = "UTF-8")
sõidu_pikkused = []
sõidu_hinnad = []
for rida in f:
    osad = rida.split(" ")
    hind = osad[2]
    
    väljumisaegh = osad[0][0:2]
    if väljumisaegh.startswith("0"):
        väljumisaegh = väljumisaegh[1]
    else:
        väljumisaegh = väljumisaegh
    väljumisaegmin = osad[0][3:5]
    if väljumisaegmin.startswith("0"):
        väljumisaegmin = väljumisaegmin[1]
    else:
        väljumisaegmin = väljumisaegmin
    väljaminutites = int(väljumisaegmin)/60
    
    
    saabumisaegh = osad[1][0:2]
    if saabumisaegh.startswith("0"):
        saabumisaegh = saabumisaegh[1]
    else:
        saabumisaegh = saabumisaegh
    saabumisaegmin = osad[1][3:5]
    if saabumisaegmin.startswith("0"):
        saabumisaegmin = saabumisaegmin[1]
    else:
        saabumisaegmin = saabumisaegmin
    sisseminutites = int(saabumisaegmin)/60
    
    arvutush = int(saabumisaegh) - int(väljumisaegh)
    arvutusmin = float(sisseminutites) - float(väljaminutites)
    if arvutusmin < 0:
        arvutush -= 1
        arvutusmin = arvutusmin * (-1)   
    aega_kulub = arvutush + arvutusmin   
    sõidu_pikkused.append(aega_kulub)
    sõidu_hinnad.append(float(hind))

lühim = min(sõidu_pikkused)
odavaim = min(sõidu_hinnad)
if aega_kulub == lühim or hind == odavaim:
    print(rida)
print(sõidu_pikkused)
print(sõidu_hinnad)