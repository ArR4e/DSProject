def sünnikuupäev(isikukood):
    kuud = ["","jaanuar", "veebruar", "märts", "aprill", "mai","juuni","juuli","august","september","oktoober","november","detsember"]
    kuupäev = isikukood[5:7]
    kuu = isikukood[3:5]
    if int(isikukood[0]) == 1 or int(isikukood[0]) == 2:
        aasta = "18" + isikukood[1:3]
    elif int(isikukood[0]) == 3 or int(isikukood[0]) == 4:
        aasta = "19" + isikukood[1:3]
    elif int(isikukood[0]) == 5 or int(isikukood[0]) == 6:
        aasta = "20" + isikukood[1:3]
    kuu = kuud[int(kuu)]
    sünnikuupäev = kuupäev + ". " + kuu + " " + aasta
    return str(sünnikuupäev)