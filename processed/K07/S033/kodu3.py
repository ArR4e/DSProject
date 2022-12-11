def sünnikuupäev(isikukood):
    kuud = ['jaanuar', 'veebruar', 'märts', 'aprill', 'mai', 'juuni', 'juuli', 'august',
        'september', 'oktoober', 'november', 'detsember']
    aasta = ""
    if isikukood[0] == str(1) or isikukood[0] == str(2):
        aasta = '18' + isikukood[1:3]
    elif isikukood[0] == str(3) or isikukood[0] == str(4):
        aasta = '19' + isikukood[1:3]
    elif isikukood[0] == str(5) or isikukood[0] == str(6):
        aasta = '20' + isikukood[1:3]
    kuunr = int(isikukood[3:5])
    kuu = str(kuud[kuunr - 1])
    päev = isikukood[5:7]
    sünnikuupäev = päev + '. ' + kuu + ' ' + aasta
    return sünnikuupäev

print(sünnikuupäev('60101017683'))
    