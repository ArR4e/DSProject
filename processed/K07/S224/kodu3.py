def sünnikuupäev(isikukood):
    aasta = isikukood[1:3]
    kuu = isikukood[3:5]
    päev = isikukood[5:7]
    mil = isikukood[0]
    n = 0
    kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober"
            , "november", "detsember"]
    
    täpnekuu = kuud[n-1]
    
    sünnikuupäev = päev + "." + täpnekuu + "." + aasta
    
    return sünnikuupäev 

print(sünnikuupäev("50010100233"))
    
    
    
    