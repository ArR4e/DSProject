def sünnikuupäev(isikukood):
    isikukood = list(isikukood)
    aastalõpp = isikukood[1] + isikukood[2]
    if int(isikukood[0]) == 3 or int(isikukood[0]) == 4:
        aasta = "19" + aastalõpp
    elif int(isikukood[0]) == 5 or int(isikukood[0]) == 6:
        aasta = "20" + aastalõpp
    else:
        aasta = "18" + aastalõpp
    
    kuunr = isikukood[3] + isikukood[4]
    if kuunr == "01":
        kuu = " jaanuar "
    elif kuunr == "02":
        kuu = " veebruar "
    elif kuunr == "03":
        kuu = " märts "
    elif kuunr == "04":
        kuu = " aprill "
    elif kuunr == "05":
        kuu = " mai "
    elif kuunr == "06":
        kuu = " juuni "
    elif kuunr == "07":
        kuu = " juuli "
    elif kuunr == "08":
        kuu = " august "
    elif kuunr == "09":
        kuu = " september "
    elif kuunr == "10":
        kuu = " oktoober "
    elif kuunr == "11":
        kuu = " november "
    else:
        kuu = " detsember "
    
    if int(isikukood[5]) > 0:
        kuupäev = isikukood[5] + isikukood[6] + "."
    else:
        kuupäev = isikukood[6] + "."
    
    return(kuupäev+ kuu + aasta)

