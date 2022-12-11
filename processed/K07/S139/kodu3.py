def sünnikuupäev(isikukood):
    päev = ""
    kuu = ""
    aasta = ""
    päev += isikukood[5]+isikukood[6]+"."
    if int(isikukood[0]) > 0 and int(isikukood[0]) <= 2:
        aasta += "18"+isikukood[1]+isikukood[2]
    if int(isikukood[0]) > 2 and int(isikukood[0]) <= 4:
        aasta += "19"+isikukood[1]+isikukood[2]
    if int(isikukood[0])>4 and int(isikukood[0]) <=6:
        aasta += "20"+isikukood[1]+isikukood[2]
    kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember",]
    if isikukood[3] == "0":
        kuu += kuud[int(isikukood[4])-1]
    elif isikukood[3] != "0":
        kuu += kuud[int(isikukood[3]+isikukood[4])-1]
    
    return " ".join([päev,kuu,aasta])
print(sünnikuupäev("19805120830"))