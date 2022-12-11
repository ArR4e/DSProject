def sünnikuupäev (isikukood):
    aasta = str(isikukood[1:3])
    kuu = str(isikukood[3:5])
    päev = str(isikukood[5:7])
    sugu = int(isikukood[0])
    if sugu == 3 or sugu == 4:
        aasta = ("19"+aasta)
    elif sugu == 5 or sugu == 6:
        aasta = ("20"+aasta)
    kuud = ["jaanuar","01","veebruar","02","märts","03","aprill","04","mai","05","juuni","06","juuli","07",
            "august","08","september","09","oktoober","10","november","11","detsember","12"]
    if kuu in kuud:
        kuu = kuud[(kuud.index(kuu)) - 1]
        kokku =str(päev + ". " + kuu + " " + aasta)
        return kokku
    
