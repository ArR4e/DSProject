def sünnikuupäev(isikukood):
    
    for rida in isikukood:
        kuupäev = rida[5:7]
        kuu = rida[3:5]
        if rida[0] == 1 or rida[0] == 2:
            aasta = "18" + isikukood[1:3]
        elif rida[0] == 3 or rida[0] == 4:
            aasta = "19" + isikukood[1:3]
        else:
            aasta = "20" + isikukood[1:3]
        sünnikuupäev = str(kuupäev) + ". " + str(kuu) + " " + aasta
        return sünnikuupäev