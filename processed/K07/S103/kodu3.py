def sünnikuupäev(isikukood):
    kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    päev = isikukood[5] + isikukood[6]
    kuu_nimi = kuud[int(isikukood[3] + isikukood[4])-1]
    if int(isikukood[0]) == 3 or int(isikukood[0]) == 4:
        aasta = "19" + isikukood[1] + isikukood[2]
    elif int(isikukood[0]) == 5 or int(isikukood[0]) == 6:
        aasta = "20" + isikukood[1] + isikukood[2]
    else:
        aasta = "18" + isikukood[1] + isikukood[2]
    sõne = päev + "." + " " + kuu_nimi + " " + aasta
    return sõne
