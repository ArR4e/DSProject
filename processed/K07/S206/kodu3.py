def sünnikuupäev(isikukood):
    kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    if int(isikukood[0]) < 3:
        aasta = "18"
    elif int(isikukood[0]) <5:
        aasta = "19"
    else:
        aasta ="20"
    aasta += isikukood[1:3]
    if isikukood[3] == "0":
        kuu = kuud[int(isikukood[4])-1]
    else:
        kuu = kuud[int(isikukood[3:5])-1]
    if isikukood[5] == "0":
        päev = isikukood[6]
    else:
        päev = isikukood[5:7]
    return f"{päev}. {kuu} {aasta}"
    
print(sünnikuupäev("60112062723"))