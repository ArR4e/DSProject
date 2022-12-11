def sünnikuupäev(isikukood):
    kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    kood = list(isikukood)
    if int(kood[5]) > 0:
        kuupäev = kood[5] + kood[6]
    else:
        kuupäev = isikukood[6]
    if int(kood[3]) > 0:
        if int(kood[4]) == 1:
            kuu = kuud[10]
        elif int(kood[4]) == 2:
            kuu = kuud[11]
        else:
            kuu = kuud[9]
    else:
        kuu = kuud[int(kood[4]) - 1]
    if int(kood[0]) < 3:
        aasta = "18" + kood[1] + kood[2]
    elif int(kood[0]) < 5:
        aasta = "19" + kood[1] + kood[2]
    else:
        aasta = "20" + kood[1] + kood[2]
    kuupäev_kuu_aasta = (kuupäev + ". " + kuu + " " + aasta)
    return kuupäev_kuu_aasta
isikukood = '29802158384'
print(sünnikuupäev(isikukood))