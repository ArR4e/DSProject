def sünnikuupäev(isikukood):
    päev = isikukood[5:7]
    if isikukood[0] == "3" or isikukood[0] == "4":
        aastaalgus = "19"
        aastalõpp = isikukood[1:3]
        aasta = aastaalgus + aastalõpp
    elif isikukood[0] == "6" or isikukood[0] == "5":
        aastaalgus = "20"
        aastalõpp = isikukood[1:3]
        aasta = aastaalgus + aastalõpp
    elif isikukood[0] == "1" or isikukood[0] == "2":
        aastaalgus = "18"
        aastalõpp = isikukood[1:3]
        aasta = aastaalgus + aastalõpp
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
    elif isikukood[2:3] == "09":
            kuu = "september"
    elif isikukood[3:5] == "10":
            kuu = "oktoober"
    elif isikukood[3:5] == "11":
        kuu = "november"
    elif isikukood[3:5] == "12":
        kuu = "detsember"
    sünnipäev = päev + ". " + kuu + " " + aasta
    return(sünnipäev)
            
    
    
    
        
        