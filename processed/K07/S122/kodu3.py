def sünnikuupäev(isikukood):
    sugu = isikukood[0]
    sünniaasta = isikukood[1] + isikukood[2]
    
    if sugu == "1" or sugu == "2":
        sünniaasta = "18" + isikukood[1] + isikukood[2]
    elif sugu == "3" or sugu == "4":
        sünniaasta = "19" + isikukood[1] + isikukood[2]
    elif sugu == "5" or sugu == "6":
        sünniaasta = "20" + isikukood[1] + isikukood[2]
    
    kuu = isikukood[3] + isikukood[4]
    päev = isikukood[5] + isikukood[6]

    if kuu == "01":
        kuu = "jaanuar"
    elif kuu == "02":
        kuu = "veebruar"
    elif kuu == "03":
        kuu = "märts"
    elif kuu == "04":
        kuu = "aprill"
    elif kuu == "05":
        kuu = "mai"
    elif kuu == "06":
        kuu = "juuni"
    elif kuu == "07":
        kuu = "juuli"
    elif kuu == "08":
        kuu = "august"
    elif kuu == "09":
        kuu = "september"
    elif kuu == "10":
        kuu = "oktoober"
    elif kuu == "11":
        kuu = "november"
    elif kuu == "12":
        kuu = "detsember"
        
    return( päev + ". " + kuu + " " + sünniaasta)
