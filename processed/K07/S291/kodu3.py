def sünnikuupäev(isikukood):
    kaksteist_kuud = ["kuu_nr_null", "jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    päev = isikukood[5:7]
    kuu = isikukood[3:5]
    if kuu[0] == "0":
        kuu_sõnadega = kaksteist_kuud[int(kuu[1])]
    else:
        kuu_sõnadega = kaksteist_kuud[int(kuu)]
    aasta = isikukood[1:3]
    if isikukood[0] == "1" or isikukood[0] == "2":
        aastaarv = "18" + aasta
    elif isikukood[0] == "3" or isikukood[0] == "4":
        aastaarv = "19" + aasta
    elif isikukood[0] == "5" or isikukood[0] == "6":
        aastaarv = "20" + aasta
    return (päev + ". " + kuu_sõnadega + " " + aastaarv)