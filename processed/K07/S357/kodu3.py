def sünnikuupäev(isikukood):
    päev = isikukood[5: 7]
    kuu_nr = isikukood[3: 5]
    aastaarv = isikukood[1: 3]
    
    kuud = ["0", "jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    kuu = kuud[int(kuu_nr)]
    
    if isikukood[0] == "1" or isikukood[0] == "2":
        aasta = ("18" + str(aastaarv))
    if isikukood[0] == "3" or isikukood[0] == "4":
        aasta = ("19" + str(aastaarv))
    if isikukood[0] == "5" or isikukood[0] == "6":
        aasta = ("20" + str(aastaarv))
    
    sünnikuupäev = (päev + ". " + kuu + " " + aasta)
    
    return sünnikuupäev
