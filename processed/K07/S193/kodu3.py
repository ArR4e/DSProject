def sünnikuupäev(isikukood):
    arv = list(isikukood)
    päev = "" .join (arv[5:7]|) + "."
    kuude_järjend = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    kuu = kuude_järjend .join(arv[3:5])
    aasta = "18" + isikukood [1:3]
    return = päev + "." + kuu + " " + aasta




isikukood = "34501234215"
sünnikuupäev(isikukood)