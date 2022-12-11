def sünnikuupäev(isikukood):
    for i in str(isikukood):
        järjend = i.split(' ')
        päev = isikukood[5:7]
        kuud = isikukood[3:5]
        kuu_järjend = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
        kuu = kuu_järjend[int(kuud)-1]
        if int(isikukood[0]) == 1 or int(isikukood[0]) == 2:
            aasta = "18" + isikukood[1:3]
        elif int(isikukood[0]) == 3 or int(isikukood[0]) == 4:
            aasta = "19" + isikukood[1:3]
        else:
            aasta = "20" + isikukood[1:3]
        sünnikuupäev = päev + ". " + kuu + " " + aasta
        return sünnikuupäev

