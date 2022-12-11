def sünnikuupäev(x):
    jär = []
    jär[:0]=x
    if jär[0] == "1" or jär[0] == "2":
        aasta=18
    elif jär[0] == "3" or jär[0] == "4":
        aasta=19
    elif jär[0] == "5" or jär[0] == "6":
        aasta = 20
    sünniaasta = x[1:3]
    kuu = {"01":"jaanuar", "02":"veebruar", "03":"märts", "04":"aprill", "05":"mai", "06":"juuni", "07":"juuli", "08":"august", "09":"september", "10":"oktoober", "11":"november", "12":"detsember"}
    sünnikuu = kuu[x[3:5]]
    päev = x[5:7]
    return (str(päev) + ". " + sünnikuu + " " + str(aasta) + sünniaasta)
print(sünnikuupäev('34501234215'))
