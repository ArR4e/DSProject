def sünnikuupäev(isikukood):
    list(isikukood)
    if isikukood[0:1] == "1" or isikukood[0:1] == "2":
        aasta = "18" + isikukood[1:3]
    if isikukood[0:1] == "3"or isikukood[0:1] == "4":
        aasta = "19" + isikukood[1:3]
    if isikukood[0:1] == "5" or isikukood[0:1] == "6":
        aasta = "20" + isikukood[1:3]
    kuu1 = isikukood[3:5]
    if isikukood[5:6] == "0":
        päev = isikukood[6:7]
    else:
        päev = isikukood[5:7]
    kuu_järjend = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    kuu = kuu_järjend[int(kuu1)- 1]
    return päev + ". " + kuu + " " + aasta
    
    