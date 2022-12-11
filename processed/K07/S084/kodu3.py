def sünnikuupäev(kood):
    esimene = int(kood[0])
    päev = kood[5]+kood[6]
    kuu = kood[3]+kood[4]
    aasta = kood[1]+kood[2]
    #Paneb kuu numbri asemele sõna
    if kuu == "01":
        kuu = "jaanuar"
    elif kuu == "02":
        kuu = "veebruar"
    elif kuu == "03":
        kuu = "märts"
    elif kuu == "04":
        kuu = "aprill"
    elif kuu == "05":
        kuu = "mai"
    elif kuu == "06":
        kuu = "juuni"
    elif kuu == "07":
        kuu = "juuli"
    elif kuu == "08":
        kuu = "august"
    elif kuu == "09":
        kuu = "september"
    elif kuu == "10":
        kuu = "oktoober"
    elif kuu == "11":
        kuu = "november"
    elif kuu == "12":
        kuu = "detsember"
    #Otsustab koodi esimese numbri järgi aasta 2 esimest numbrit
    if esimene == 1 or esimene == 2:
        aasta = "18" + aasta
    elif esimene == 3 or esimene == 4:
        aasta = "19" + aasta
    elif esimene == 5 or esimene == 6:
        aasta = "20" + aasta
    elif esimene == 7 or esimene == 8:
        aasta = "21" + aasta
    return päev + ". " + kuu + " " + aasta
print(sünnikuupäev("34501234215"))