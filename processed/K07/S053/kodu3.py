def sünnikuupäev(isikukood):
    sünniaasta = isikukood [1:3]
    if isikukood[0] == "1" or isikukood[0] == "2":
        aasta = "18" + sünniaasta
    elif isikukood[0] == "3" or isikukood[0] == "4":
        aasta = "19" + sünniaasta
    elif isikukood[0] == "5" or isikukood[0] == "6":
        aasta = "20" + sünniaasta
    kuupäev = isikukood[5:7]
    kuu = isikukood [3:5]
    kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    kuunimi = kuud[int(kuu)-1]
    return (str(kuupäev) + ". " + str(kuunimi) + " " + str(aasta))

