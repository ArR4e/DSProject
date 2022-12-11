def sünnikuupäev(isikukood):
    aasta = isikukood[1]+isikukood[2]
    kuu = isikukood[3]+isikukood[4]
    päev = isikukood[5]+isikukood[6]
    kuupäev = ""
    if isikukood[0] == "3" or isikukood[0] == "4":
        kuupäev = päev + ".", kuud[int(kuu)-1], "19" + aasta
    elif isikukood[0] == "5" or isikukood[0] == "6":
        kuupäev = päev + ".", kuud[int(kuu)-1], "20" + aasta
    else:
        kuupäev = päev + ".", kuud[int(kuu)-1], "18" + aasta
    return kuupäev[0]+" "+kuupäev[1]+" "+kuupäev[2]

kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]