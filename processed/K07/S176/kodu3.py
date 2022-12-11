kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli",
        "august", "september", "oktoober", "november", "detsember"]
def sünnikuupäev(isikukood):
    
    päev = isikukood[5:7] + ". "
    kuu = kuud[int(isikukood[3:5]) - 1] + " "
    aasta = isikukood[1:3]
    if isikukood[0] == "1" or isikukood[0] == "2":
        aasta = "18" + isikukood[1:3]
    elif isikukood[0] == "3" or isikukood[0] == "4":
        aasta = "19" + isikukood[1:3]
    elif isikukood[0] == "5" or isikukood[0] == "6":
        aasta = "20" + isikukood[1:3]
    
    return (päev+kuu+aasta)
