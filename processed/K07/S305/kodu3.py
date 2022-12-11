def sünnikuupäev(a):
    päev = a[5:7]
    kuu = a[3:5]
    aasta = a[1:3]
    if int(a[0]) == 1 or int(a[0]) == 2:
        aasta = "18" + aasta
    elif int(a[0]) == 3 or int(a[0]) == 4:
        aasta = "19" + aasta
    elif int(a[0]) == 5 or int(a[0]) == 6:
        aasta = "20" + aasta
    kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    kuu = kuud[int(kuu)-1]
    return (päev + ". " + kuu + " " + aasta)
print(sünnikuupäev("34501234215"))