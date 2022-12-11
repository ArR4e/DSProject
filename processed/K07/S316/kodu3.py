def sünnikuupäev(isikukood):
    kuupäev = ""
    kuupäev = kuupäev + isikukood[5:7] + "."
    if isikukood[3:5] == "01":
        kuupäev += " jaanuar "
    elif isikukood[3:5] == "02":
        kuupäev += " veebruar "
    elif isikukood[3:5] == "03":
        kuupäev += " märts "
    elif isikukood[3:5] == "04":
        kuupäev += " aprill "
    elif isikukood[3:5] == "05":
        kuupäev += " mai "
    elif isikukood[3:5] == "06":
        kuupäev += " juuni "
    elif isikukood[3:5] == "07":
        kuupäev += " juuli "
    elif isikukood[3:5] == "08":
        kuupäev += " august "
    elif isikukood[3:5] == "09":
        kuupäev += " september "
    elif isikukood[3:5] == "10":
        kuupäev += " oktoober "
    elif isikukood[3:5] == "11":
        kuupäev += " november "
    elif isikukood[3:5] == "12":
        kuupäev += " detsember "
    if isikukood[0] == "1" or isikukood[0] == "2":
        kuupäev += "18"
    elif isikukood[0] == "3" or isikukood[0] == "4":
        kuupäev += "19"
    elif isikukood[0] == "5" or isikukood[0] == "6":
        kuupäev += "20"
    kuupäev += isikukood[1:3]
    return kuupäev