def sünnikuupäev(isikukood):

    kuu = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    if int(isikukood[0]) < 3:
        aasta = " 18" + isikukood[1:3]
    elif int(isikukood[0]) < 5:
        aasta = " 19" + isikukood[1:3] 
    else:
        aasta = " 20" + isikukood[1:3]
    kuu = kuu[int(isikukood[3:5])-1]
    päev = isikukood[5:7] + ". "
    kuupäev = päev + kuu + aasta
    return kuupäev
sisend = input("Sisesta isikukood: ")
print(sünnikuupäev(sisend))