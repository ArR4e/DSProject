isikukood = input("Sisesta oma isikukood: ")
def sünnikuupäev(isikukood) :
    #kuupäev
    kuupäev = int(isikukood[5:7])
    #kuu
    kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    kuu = kuud[int(isikukood[3:5])-1]
    #aasta
    if int(isikukood[0]) < 3:
        aasta = "18" + isikukood[1:3]
    elif int(isikukood[0]) < 5:
        aasta = "19" + isikukood[1:3]
    elif int(isikukood[0]) < 7:
        aasta = "20" + isikukood[1:3]

    return str(kuupäev) + ". " + str(kuu) + " " + str(aasta)
print(sünnikuupäev(isikukood))