kuud = ["jaanuar","veebruar","märts","aprill","mai","juuni","juuli","august","september","oktoober","november","detsember"]
def sünnikuupäev(isikukood):
    x = isikukood[0]
    if x == "1" or x == "2":
        aasta = 1800
    elif x == "3" or x == "4":
        aasta = 1900
    elif x == "5" or x == "6":
        aasta = 2000
    x = isikukood[1] + isikukood[2]
    aasta = aasta + int(x)
    if isikukood[3] == 0:
        kuu = kuud[int(isikukood[4])-1]
    else:
        x = isikukood[3] + isikukood[4]
        kuu = kuud[int(x)-1]
    if isikukood[5] == 0:
        päev = int(isikukood[6])
    else:
        päev = int(isikukood[5]+isikukood[6])
        
    sünnipäev = str(päev)+". "+kuu+" "+str(aasta)
    return sünnipäev