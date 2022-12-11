def sünnikuupäev(isikukood):
    päev = isikukood[5] + isikukood[6]
    kuu_numbriga = isikukood[3] + isikukood[4]
    if kuu_numbriga == '01':
        kuu = 'jaanuar'
    elif kuu_numbriga == '02':
        kuu = 'veebruar'
    elif kuu_numbriga == '03':
        kuu = 'märts'
    elif kuu_numbriga == '04':
        kuu = 'aprill'
    elif kuu_numbriga == '05':
        kuu = 'mai'
    elif kuu_numbriga == '06':
        kuu = 'juuni'
    elif kuu_numbriga == '07':
        kuu = 'juuli'
    elif kuu_numbriga == '08':
        kuu = 'august'
    elif kuu_numbriga == '09':
        kuu = 'september'
    elif kuu_numbriga == '10':
        kuu = 'oktoober'
    elif kuu_numbriga == '11':
        kuu = 'november'
    elif kuu_numbriga == '12':
        kuu = 'detsember'
    aasta_viimased = isikukood[1] + isikukood[2]
    aasta = ''
    if isikukood[0] == '1' or isikukood[0] == '2':
        aasta += '18'
    if isikukood[0] == '3' or isikukood[0] == '4':
        aasta += '19'
    if isikukood[0] == '5' or isikukood[0] == '6':
        aasta += '20'
    if isikukood[0] == '7' or isikukood[0] == '8':
        aasta += '21'
    aasta += aasta_viimased
    return päev + '. ' + kuu + ' ' + aasta