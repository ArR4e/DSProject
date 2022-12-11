def kuu_arvutamine(nr):
    if nr == 1:
        return 'jaanuar'
    if nr == 2:
        return 'veebruar'
    if nr == 3:
        return 'märts'
    if nr == 4:
        return 'aprill'
    if nr == 5:
        return 'mai'
    if nr == 6:
        return 'juuni'
    if nr == 7:
        return 'juuli'
    if nr == 8:
        return 'august'
    if nr == 9:
        return 'september'
    if nr == 10:
        return 'oktoober'
    if nr == 11:
        return 'november'
    if nr == 12:
        return 'detsember'
    return None

def sünnikuupäev(isikukood):
    isikulist = ' '.join(isikukood).split()
    if int(isikulist[0]) == 1 or int(isikulist[0]) == 2:
        aasta = '18' + isikulist[1] + isikulist[2]
    elif int(isikulist[0]) == 3 or int(isikulist[0]) == 4:
        aasta = '19' + isikulist[1] + isikulist[2]
    else:
        aasta = '20' + isikulist[1] + isikulist[2]
    kuu = kuu_arvutamine(int(isikulist[3] + isikulist[4]))
    päev = str(int(isikulist[5] + isikulist[6])) + '.'
    return päev + ' ' + kuu + ' ' + aasta

isikukood = input('Sisestage isikukood: ')

print(sünnikuupäev(isikukood))