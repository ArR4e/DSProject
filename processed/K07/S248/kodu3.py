def sünnikuupäev(isikood):
    kuulist = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    for i in range(0,len(kuulist)):
        if int(isikood[3:5]) == i+1:
            kuu = kuulist[i]
    if int(isikood[0]) > 4:
        aasta = "20"+str(isikood[1:3])
    elif int(isikood[0]) < 3:
        aasta = "18"+str(isikood[1:3])
    else:
        aasta = "19"+str(isikood[1:3])
    
    return isikood[5:7] + ". " + kuu + " " + aasta
    