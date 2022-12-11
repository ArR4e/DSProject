isikukood = input("Sisesta isikukood: ")

def sünnikuupäev(isikukood):
    
    if isikukood[0] == "1" or isikukood[0] == "2":
        aastatuhat = 1800
    elif isikukood[0] == "3" or isikukood[0] == "4":
        aastatuhat = 1900
    elif isikukood[0] == "5" or isikukood[0] == "6":
        aastatuhat = 2000
    elif isikukood[0] == "7" or isikukood[0] == "8":
        aastatuhat = 2100
    
    aastakümme = isikukood[1:3]
    aasta = int(aastatuhat) + int(aastakümme)
    
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
    elif isikukood[3:5] == "12":
        kuu = "detsember"
    
    kuupäev = isikukood[5:7]
    lause = kuupäev + ". " + kuu + " " + str(aasta)
    return lause
    
sünnikuupäev(isikukood)