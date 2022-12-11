def sünnikuupäev(isikukood):
    sugu = isikukood[0]
    päev = isikukood[5:7]
    kuu = isikukood[3:5]
    aasta = isikukood[1:3]
    
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

        
    
    if sugu == "1" or sugu == "2":
        aasta = "18" + aasta
    elif sugu == "3" or sugu == "4":
        aasta = "19" + aasta
    elif sugu == "5" or sugu == "6":
        aasta = "20" + aasta
    return(päev + "." + " " + kuu +" " + aasta)
print(sünnikuupäev('34501234215'))
    