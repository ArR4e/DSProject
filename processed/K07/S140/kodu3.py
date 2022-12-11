def sünnikuupäev(isikukood):
    kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    i = isikukood[0]
    if i == "1" or i == "2":
        aasta = 1800 + int(isikukood[1:3])
    elif i == "3" or i == "4":
        aasta = 1900 + int(isikukood[1:3])
    elif i == "5" or i == "6":
        aasta = 2000 + int(isikukood[1:3])
    else:
        aasta = 2100 + int(isikukood[1:3])
    
    kuu = kuud[int(isikukood[3:5]) - 1]
    päev = isikukood[5:7]
    
    tulemus = "{0}. {1} {2}".format(päev, kuu, aasta)
    return tulemus
