def sünnikuupäev(isikukood):
    aasta = ""
    
    if isikukood[0] == "1" or isikukood[0] == "2":
        aasta += "18"
    elif isikukood[0] == "3" or isikukood[0] == "4":
        aasta += "19"
    elif isikukood[0] == "5" or isikukood[0] == "6":
        aasta += "20"
        
    aasta += isikukood[1] + isikukood[2]
    
    kuu = isikukood[3] + isikukood[4]
    kuu_result = ""
    
    if kuu == "01":
        kuu_result += "jaanuar"
    elif kuu == "02":
        kuu_result += "veebruar"
    elif kuu == "03":
        kuu_result += "märts"
    elif kuu == "04":
        kuu_result += "aprill"
    elif kuu == "05":
        kuu_result += "mai"
    elif kuu == "06":
        kuu_result += "juuni"
    elif kuu == "07":
        kuu_result += "juuli"
    elif kuu == "08":
        kuu_result += "august"
    elif kuu == "09":
        kuu_result += "september"
    elif kuu == "10":
        kuu_result += "oktoober"
    elif kuu == "11":
        kuu_result += "november"
    elif kuu == "12":
        kuu_result += "detsember"
    
    päev = isikukood[5] + isikukood[6] 
        
    return päev + ". " + kuu_result + " " + aasta
        