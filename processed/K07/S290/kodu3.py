def sünnikuupäev(isikukood):
    päev = isikukood[5:7]
    aasta = isikukood[1:3]
    kuu = isikukood[3:5]
    
    if isikukood[0] == "3":
        aasta = str("19")+ str(aasta)
    elif isikukood[0] == "4":
        aasta = str("19")+ str(aasta)
    elif isikukood[0] == "1":
        aasta = str("18") + str(aasta) 
    elif isikukood[0] == "2":
        aasta = str("18") + str(aasta)
    else:
        aasta = str("20")+ str(aasta)
        
    if str(kuu) == "12":
        kuu = "detsember"
    elif str(kuu) == "11":
        kuu = "november"
    elif str(kuu) == "10":
        kuu = "oktoober"
    elif str(kuu) == "09":
        kuu = "september"
    elif str(kuu) == "08":
        kuu = "august"
    elif str(kuu) == "07":
        kuu = "juuli"
    elif str(kuu) == "06":
        kuu = "juuni"
    elif str(kuu) == "05":
        kuu = "mai"
    elif str(kuu) == "04":
        kuu = "aprill"
    elif str(kuu) == "03":
        kuu = "märts"
    elif str(kuu) == "02":
        kuu = "veebruar"
    elif str(kuu) == "01":
        kuu = "jaanuar"
        
    if isikukood[5] == "0":
        päev = isikukood[6]
        
        
    sünnikuupäev = päev + ". " + kuu + " " + aasta
    return(sünnikuupäev)
    
    