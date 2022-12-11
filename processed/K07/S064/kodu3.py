def sünnikuupäev(isikukood):
    list(isikukood)
    sünniaasta = isikukood[1:3]
    sünnikuu = isikukood[3:5]
    päev = isikukood[5:7]
    if int(isikukood[0]) == 1 or int(isikukood[0]) == 2:
        aasta = "18" + str(sünniaasta)
    elif int(isikukood[0]) == 3 or int(isikukood[0]) == 4:
        aasta = "19" + str(sünniaasta)
    elif int(isikukood[0]) == 5 or int(isikukood[0]) == 6:
        aasta = "20" + str(sünniaasta)
        
    if sünnikuu == "01":
        sünnikuu = "jaanuar"
    elif sünnikuu == "02":
        sünnikuu = "veebruar"
    elif sünnikuu == "03":
        sünnikuu = "märts"
    elif sünnikuu == "04":
        sünnikuu = "aprill"
    elif sünnikuu == "05":
        sünnikuu = "mai"
    elif sünnikuu == "06":
        sünnikuu = "juuni"
    elif sünnikuu == "07":
        sünnikuu = "juuli"
    elif sünnikuu == "08":
        sünnikuu = "august"
    elif sünnikuu == "09":
        sünnikuu = "september"
    elif sünnikuu == "10":
        sünnikuu = "oktoober"
    elif sünnikuu == "11":
        sünnikuu = "november"
    elif sünnikuu == "12":
        sünnikuu = "detsember"
        
    sünnikuupäev = päev + ". " + sünnikuu + " " + aasta
    return(sünnikuupäev)
print(sünnikuupäev("34501234215"))