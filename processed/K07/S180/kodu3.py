def sünnikuupäev(isikukood):
    kuud = ['jaanuar', 'veebruar', 'märts', 'aprill', 'mai', 'juuni', 'juuli', 'august', 'september', 'oktoober', 'november', 'detsember']
    list(isikukood)
    if isikukood[0] == '3' or isikukood[0] == '4':
        aasta = '19' + isikukood[1] + isikukood[2]
    elif isikukood[0] == '5' or isikukood[0] == '6':
        aasta = '20' + isikukood[1] + isikukood[2]
    elif isikukood[0] == '2' or isikukood[0] == '1':
        aasta = '18' + isikukood[1] + isikukood[2]
    kuu = kuud[int(isikukood[3] + isikukood[4]) - 1]
    päev = isikukood[5] + isikukood[6]
    return (päev + '.' + ' ' + kuu + ' ' + aasta)