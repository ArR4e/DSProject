def sünnikuupäev(isikukood):
    kood = list(isikukood)
    paev = kood[5] + kood [6]
    kuu = int(kood[3] + kood[4])
    aasta = (kood[1] + kood[2])
    esimene = int(kood[0])
    if esimene == 1 or esimene == 2:
        aasta = "18" + aasta
    elif esimene == 3 or esimene == 4:
        aasta = "19" + aasta
    else:
        aasta = "20" + aasta
    if kuu == 1:
        kuu = "jaanuar"
    elif kuu == 2:
        kuu = "veebruar"
    elif kuu == 3:
        kuu = "märts"
    elif kuu == 4:
        kuu = "aprill"
    elif kuu == 5:
        kuu = "mai"
    elif kuu == 6:
        kuu = "juuni"
    elif kuu == 7:
        kuu = "juuli"
    elif kuu == 8:
        kuu = "august"
    elif kuu == 9:
        kuu = "september"
    elif kuu == 10:
        kuu = "oktoober"
    elif kuu == 11:
        kuu = "november"
    else:
        kuu = "detsember"
    synna = paev + ". " + kuu + " " + aasta
    return synna
sünnikuupäev('39703152701')   