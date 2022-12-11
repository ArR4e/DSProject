def sünnikuupäev(isikukood):
    aasta = str(isikukood[1]) + str(isikukood[2])
    kuu1 = int((isikukood[3]) + (isikukood[4]))
    päev = str(isikukood[5]) + str(isikukood[6])
    kuud = ['jaanuar','veebruar','märts','aprill','mai','juuni','juuli','august','september','oktoober','november','detsember']
    kuu = kuud[kuu1-1]
    
    if isikukood[0] == '1' or isikukood[0] == '2':
        aasta = '18' + aasta
        kokku = päev + ". " + kuu + " " + aasta
        return(kokku)
    
    elif isikukood[0] == '3' or isikukood[0] == '4':
        aasta = '19' + aasta
        kokku = päev + ". " + kuu + " " + aasta
        return(kokku)
    
    elif isikukood[0] == '5' or isikukood[0] == '6':
        aasta = '20' + aasta
        kokku = päev + ". " + kuu + " " + aasta
        return(kokku)
    
    elif isikukood[0] == '7' or isikukood[0] == '8':
        aasta = '20' + aasta
        kokku = päev + ". " + kuu + " " + aasta
        return(kokku)