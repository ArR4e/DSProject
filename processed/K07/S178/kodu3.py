def sünnikuupäev(isikukood):
    algkood = int(isikukood[0:1])
    aasta = int(isikukood[1:3])
    kuu = int(isikukood[3:5])
    kuupäev = int(isikukood[5:7])
    if algkood == 6 or algkood == 5:
        aasta2 = 2000 + aasta
    elif algkood == 4 or algkood == 3:
        aasta2 = 1900 + aasta
    else:
        aasta2 = 1800 + aasta
    if kuu == 1:
        kuu2 = ('jaanuar')
    elif kuu == 2:
        kuu2 = ('veebruar')
    elif kuu == 3:
        kuu2 = ('märts')
    elif kuu == 4:
        kuu2 = ('aprill')
    elif kuu == 5:
        kuu2 = ('mai')
    elif kuu == 6:
        kuu2 = ('juuni')
    elif kuu == 7:
        kuu2 = ('juuli')
    elif kuu == 8:
        kuu2 = ('august')
    elif kuu == 9:
        kuu2 = ('september')
    elif kuu == 10:
        kuu2 = ('oktoober')
    elif kuu == 11:
        kuu2 = ('november')
    else:
        kuu2 = ('detsember')
    sisu = ' '.join([str(kuupäev) + '.', kuu2 + ' ' + str(aasta2)])
    return (sisu)


isikukood = input('Sisesta isikukood: ')
print(sünnikuupäev(isikukood))