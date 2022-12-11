kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
def sünnikuupäev(x):
    päev = x[5:7]
    kuu_nr = int(x[3:5])
    kuu = kuud[kuu_nr - 1]
    if x[0] == "1" or x[0] == "2":
        aasta = "18" + str(x[1:3])
    elif x[0] == "3" or x[0] == "4":
        aasta = "19" + str(x[1:3])
    elif x[0] == "5" or x[0] == "6":
        aasta = "20" + str(x[1:3])
    return str(päev) + ". " + str(kuu) + " " + str(aasta)
    print(sünnikuupäev)