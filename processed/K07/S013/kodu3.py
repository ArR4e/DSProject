isikukood = str(input("ik "))
def sünnikuupäev(isikukood):
    päev = int(isikukood[5:7])
    kuu = int(isikukood[3:5])
    aasta = int(isikukood[1:3])
    sajand = int(isikukood[0])
    
    kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    kuu1 = kuu - 1
    kuu2 = kuud[kuu1]
    
    if sajand < 3:
        aasta1 = "18" + str(aasta)
        kokku = str(päev) + ". " + str(kuu2) + " " + str(aasta1)
        return kokku
    elif sajand < 5:
        aasta1 = "19" + str(aasta)
        kokku = str(päev) + ". " + str(kuu2) + " " + str(aasta1)
        return kokku
    elif sajand < 7:
        aasta1 = "20" + str(aasta)
        kokku = str(päev) + ". " + str(kuu2) + " " + str(aasta1)
        return str(kokku)

print(sünnikuupäev(isikukood))