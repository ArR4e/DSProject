
def sünnikuupäev(isikukood):
    aasta = ""
    kuu = ""
    if isikukood[0] == "1" or isikukood[0] == "2":
        aasta+="18"
    elif isikukood[0] == "3" or isikukood[0] == "4":
        aasta+="19"
    elif isikukood[0] == "5" or isikukood[0] == "6":
        aasta+="20"
    aasta+=isikukood[1]+isikukood[2]
    if isikukood[3] == "0" and isikukood[4] == "1":
        kuu = "jaanuar"
    elif isikukood[3] == "0" and isikukood[4] == "2":
        kuu = "veebruar"
    elif isikukood[3] == "0" and isikukood[4] == "3":
        kuu = "märts"
    elif isikukood[3] == "0" and isikukood[4] == "4":
        kuu = "aprill"
    elif isikukood[3] == "0" and isikukood[4] == "5":
        kuu = "mai"
    elif isikukood[3] == "0" and isikukood[4] == "6":
        kuu = "juuni"
    elif isikukood[3] == "0" and isikukood[4] == "7":
        kuu = "juuli"
    elif isikukood[3] == "0" and isikukood[4] == "8":
        kuu = "august"
    elif isikukood[3] == "0" and isikukood[4] == "9":
        kuu = "september"
    elif isikukood[3] == "1" and isikukood[4] == "0":
        kuu = "oktoober"
    elif isikukood[3] == "1" and isikukood[4] == "1":
        kuu = "november"
    elif isikukood[3] == "1" and isikukood[4] == "2":
        kuu = "detsember"
    
    return(isikukood[5]+isikukood[6]+". " + kuu + " " + aasta)

#print(sünnikuupäev("50208050815"))