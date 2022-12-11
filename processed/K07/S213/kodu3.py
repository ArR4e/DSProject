def sünnikuupäev(isikukood):
    
    päev = isikukood[5:7]
    
    kuu_list = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    kuu = kuu_list[int(isikukood[3:5]) - 1]
    
    aasta = ""
    sajand = isikukood[0:1]
    
    if sajand == "1" or sajand == "2":
        aasta += "18" + isikukood[1:3]
    elif sajand == "3" or sajand == "4":
        aasta += "19" + isikukood[1:3]
    elif sajand == "5" or sajand == "6":
        aasta += "20" + isikukood[1:3]
    elif sajand == "7" or sajand == "8":
        aasta += "21" + isikukood[1:3]
    
    return päev + ". " + kuu + " " + aasta

print(sünnikuupäev("60101017683"))
    