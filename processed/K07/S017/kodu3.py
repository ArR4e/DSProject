def sünnikuupäev(isikukood):
    päev = isikukood[5:7]
    kuunimi = isikukood[3:5]
    if kuunimi == "01":
        kuunimi = "jaanuar"
    elif kuunimi == "02":
        kuunimi = "veebruar"
    elif kuunimi == "03":
        kuunimi = "märts"
    elif kuunimi == "04":
        kuunimi = "aprill"
    elif kuunimi == "05":
        kuunimi = "mai"
    elif kuunimi == "06":
        kuunimi = "juuni"
    elif kuunimi == "07":
        kuunimi = "juuli"
    elif kuunimi == "08":
        kuunimi = "august"
    elif kuunimi == "09":
        kuunimi = "september"
    elif kuunimi == "10":
        kuunimi = "oktoober"
    elif kuunimi == "11":
        kuunimi = "november"
    elif kuunimi == "12":
        kuunimi = "detsember"
    sajand = isikukood[0]
    if sajand == "3" or sajand == "4":
        aasta = "19" + isikukood[1:3]
    elif sajand == "5" or sajand == "6":
        aasta = "20" + isikukood[1:3]
    elif sajand == "1" or sajand == "2":
        aasta = "18" + isikukood[1:3]
    return päev + ". " + kuunimi + " " + aasta

