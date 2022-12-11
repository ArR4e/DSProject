def sünnikuupäev(isikukood):
    sajand = isikukood[:1]
    aasta  = isikukood[1:3]
    kuu    = isikukood[3:5]
    päev   = isikukood[5:7]
    
    # sünniaasta leidmine
    if sajand == "1" or sajand == "2":
        a = " 18" + aasta
    elif sajand == "3" or sajand == "4":
        a = " 19" + aasta
    elif sajand == "5" or sajand == "6":
        a = " 20" + aasta
    # sünnikuu leidmine
    if kuu == "01":
        k = " jaanuar"
    elif kuu == "02":
        k = " veebruar"
    elif kuu == "03":
        k = " märts"
    elif kuu == "04":
        k = " aprill"
    elif kuu == "05":
        k = " mai"
    elif kuu == "06":
        k = " juuni"
    elif kuu == "07":
        k = " juuli"
    elif kuu == "08":
        k = " august"
    elif kuu == "09":
        k = " september"
    elif kuu == "10":
        k = " oktoober"
    elif kuu == "11":
        k = " november"
    elif kuu == "12":
        k = " detsember"
    
    # päev
    p = päev + "."
    
    # leian kuupäeva
    kuupäev = p + k + a
    return kuupäev

print(sünnikuupäev("29802158384"))