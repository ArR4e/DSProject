def sünnikuupäev(isikukood):
    list(isikukood)
    aasta = " "
    kuud = ["jaanuar","veebruar","märts","aprill","mai","juuni","juuli","august","september","oktoober","november","detsember"]
    kuu = " "
    päev = isikukood[5]+isikukood[6]+". "
    if int(isikukood[0]) < 3:
        aasta += "18"
    elif int(isikukood[0]) >= 3 and int(isikukood[0]) < 5:
        aasta += "19"
    elif int(isikukood[0]) >= 5 and int(isikukood[0]) <7:
        aasta += "20"
    else:
        aasta += "21"
    aasta += isikukood[1]+isikukood[2]
    if isikukood[3] + isikukood[4] == "01":
        kuu = kuud[0]
    elif isikukood[3] + isikukood[4] == "02":
        kuu = kuud[1]
    elif isikukood[3] + isikukood[4] == "03":
        kuu = kuud[2]
    elif isikukood[3] + isikukood[4] == "04":
        kuu = kuud[3]
    elif isikukood[3] + isikukood[4] == "05":
        kuu = kuud[4]
    elif isikukood[3] + isikukood[4] == "06":
        kuu = kuud[5]
    elif isikukood[3] + isikukood[4] == "07":
        kuu = kuud[6]
    elif isikukood[3] + isikukood[4] == "08":
        kuu = kuud[7]
    elif isikukood[3] + isikukood[4] == "09":
        kuu = kuud[8]
    elif isikukood[3] + isikukood[4] == "10":
        kuu = kuud[9]
    elif isikukood[3] + isikukood[4] == "11":
        kuu = kuud[10]
    else:
        kuu = kuud[11]
    return päev + kuu + aasta