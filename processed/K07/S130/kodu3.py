def sünnikuupäev(isikukood):
    kuupaev = isikukood[5:7]
    kuu = int(isikukood[3:5])
    kuude_jarjend = ['jaanuar', 'veebruar', 'märts', 'aprill', 'mai', 'juuni', 'juuli', 'august', 'september', 'oktoober', 'november', 'detsember']
    kuunimi = kuude_jarjend[kuu-1]
    sajand = int(isikukood[0])
    if sajand == 1:
        aasta = '18' + (isikukood[1:3])
    elif sajand == 2:
        aasta = '18' + (isikukood[1:3])
    elif sajand == 3:
        aasta = '19' + (isikukood[1:3])
    elif sajand == 4:
        aasta = '19' + (isikukood[1:3])
    else:
        aasta = '20' + (isikukood[1:3])
    return kuupaev + '. ' + kuunimi + ' ' + aasta

