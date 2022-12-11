
def sünnikuupäev(isikukood):
    kuupäev = ""
    if isikukood[0] == "1" or isikukood[0] == "2":
        aasta1 = "18"
    elif isikukood[0] == "3" or isikukood[0] == "4":
        aasta1 = "19"
    else:
        aasta1 = "20"
    
    aasta2 = isikukood[1:3]
    
    if isikukood[3:5] == "01":
        kuu = "jaanuar"
    elif isikukood[3:5] == "02":
        kuu = "veebruar"
    elif isikukood[3:5] == "03":
        kuu = "märts"
    elif isikukood[3:5] == "04":
        kuu = "aprill"
    elif isikukood[3:5] == "05":
        kuu = "mai"
    elif isikukood[3:5] == "06":
        kuu = "juuni"
    elif isikukood[3:5] == "07":
        kuu = "juuli"
    elif isikukood[3:5] == "08":
        kuu = "august"
    elif isikukood[3:5] == "09":
        kuu = "september"
    elif isikukood[3:5] == "10":
        kuu = "oktoober"
    elif isikukood[3:5] == "11":
        kuu = "november"
    else:
        kuu = "detsember"
    
    päev = isikukood[5:7]
    
    kuupäev += päev + ". " + kuu + " " + aasta1 + aasta2
    return kuupäev
