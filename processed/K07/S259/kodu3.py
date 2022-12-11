def sünnikuupäev(algneisikukood):
    kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    isikukood = []
    for i in algneisikukood:
        isikukood.append(i)
    
    aasta2nr = isikukood[0]
    if aasta2nr == "5" or aasta2nr == "6":
        aasta2nr = "20"
    elif aasta2nr == "3" or aasta2nr == "4":
        aasta2nr = "19"
    else:
        aasta2nr = '18'
    isikukood.pop(0) #removes an item at a specified index value from a list
    for i in range(4):
        isikukood.pop(-1)
    
    if int(isikukood[0] + isikukood[1]) > 20:
        aasta = aasta2nr + isikukood[0] + isikukood[1]
    else:
        aasta = aasta2nr + isikukood[0] + isikukood[1]
    
    del isikukood[0:2] #deleting objects
    kuu = kuud[int(isikukood[0]+isikukood[1])-1]
    
    del isikukood [0:2]
    päev = isikukood[0]+isikukood[1]
    
    kuupäev = (f'{päev}. {kuu} {aasta}')
    
    return kuupäev