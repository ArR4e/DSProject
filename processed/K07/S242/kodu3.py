def sünnikuupäev(isikukood):
    isikukood = list(isikukood)
    päev = isikukood[5] + isikukood[6]
    if int(isikukood[0]) < 3:
        aasta = '18' + isikukood[1] + isikukood[2]
    elif 3 <= int(isikukood[0]) < 5:
        aasta = '19' + isikukood[1] + isikukood[2]
    elif 5 <= int(isikukood[0]) < 7:
        aasta = '20' + isikukood[1] + isikukood[2]
        
    if int(isikukood[3] + isikukood[4]) == 1:
        kuu = 'jaanuar'
    elif int(isikukood[3] + isikukood[4]) == 2:
        kuu = 'veebruar'
    elif int(isikukood[3] + isikukood[4]) == 3:
        kuu = 'märts'
    elif int(isikukood[3] + isikukood[4]) == 4:
        kuu = 'aprill'
    elif int(isikukood[3] + isikukood[4]) == 5:
        kuu = 'mai'
    elif int(isikukood[3] + isikukood[4]) == 6:
        kuu = 'juuni'
    elif int(isikukood[3] + isikukood[4]) == 7:
        kuu = 'juuli'
    elif int(isikukood[3] + isikukood[4]) == 8:
        kuu = 'august'
    elif int(isikukood[3] + isikukood[4]) == 9:
        kuu = 'september'
    elif int(isikukood[3] + isikukood[4]) == 10:
        kuu = 'oktoober'
    elif int(isikukood[3] + isikukood[4]) == 11:
        kuu = 'november'
    elif int(isikukood[3] + isikukood[4]) == 12:
        kuu = 'detsember'
    
    return päev + ". " + kuu + " " + aasta
        

        