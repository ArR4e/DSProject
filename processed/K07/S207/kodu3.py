def sünnikuupäev(isikukood):
    if isikukood[5:7].startswith("0"):
        kuupäev = isikukood[6]
    else:
        kuupäev = isikukood[5:7]

    kuud = ["jaanuar","veebruar","märts","aprill","mai","juuni","juuli","august","september","oktoober","november","detsember"]
    if isikukood[6:8].startswith("0"):
        kuu = kuud[int(isikukood[4])-1]
    else:
        kuu = kuud[int(isikukood[3:5])-1]
        
    if isikukood.startswith("3") or isikukood.startswith("4"):
        aasta = "19" + isikukood[1:3]
    elif isikukood.startswith("1") or isikukood.startswith("2"):
        aasta = "18" + isikukood[1:3]    
    else:
        aasta = "20" + isikukood[1:3]
        
    return f"{kuupäev}. {kuu} {aasta}"