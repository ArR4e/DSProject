def sünnikuupäev(isikukood):
    kuud = ["Jaanuar","Veebruar","Märts","Aprill","Mai", "Juuni", "Juuli", "August", "September", "Oktoober", "November","Detsember"]
    päev = isikukood[5:7]
    kuu = isikukood[3:5]
    aasta = [isikukood[0], isikukood[1:3]]
    if int(aasta[0]) < 3:
        aasta = "18" + aasta[1]
    elif int(aasta[0]) < 5:
        aasta = "19" + aasta[1]
    else:
        aasta = "20" + aasta[1]
    if päev[0] == "0":
        päev = päev[1]
    string = päev + ". " + kuud[int(kuu)-1].lower() + " " + aasta
    return string