def sünnikuupäev(isikukood):
    arv = isikukood[0]
    aasta2 = isikukood[1:3]
    kuu = isikukood[3:5]
    päev = isikukood[5:7]
    if arv == "1" or arv == "2":
        aasta = 18
    elif arv == "3" or arv == "4":
        aasta = 19
    elif arv == "5" or arv == "6":
        aasta = 20
    else:
        aasta = 21
    
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
    sünnikuupäev = päev + "."+ " " + kuu + " " + str(aasta)+aasta2
    return sünnikuupäev
    
    
     
sünnikuupäev('34501234215')