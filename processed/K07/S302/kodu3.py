def sünnikuupäev(kood):
    aasta = 0
    kuu = 0
    kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    päev = 0
    if kood[0] == "1" or kood[0] == "2":
        aasta = 1800
    elif kood[0] == "3" or kood[0] == "4":
        aasta = 1900
    elif kood[0] == "5" or kood[0] == "6":
        aasta = 2000
    elif kood[0] == "7" or kood[0] == "8":
        aasta = 2100
    aasta += int(kood[1] + kood[2])
    kuu = int(kood[3] + kood[4])
    päev = int(kood[5] + kood[6])
    lopp = (str(päev) + ". " + str(kuud[kuu-1]) + " " +str(aasta))
    return lopp
    