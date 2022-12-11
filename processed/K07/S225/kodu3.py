def sünnikuupäev(isikukood):
    numbrid = []
    for i in isikukood:
        numbrid.append(i)
    if numbrid[0] == '1' or numbrid[0] == '2':
        aasta = ('18' + numbrid[1] + numbrid[2])
    elif numbrid[0] == '3' or numbrid[0] == '4':
        aasta = ('19' + numbrid[1] + numbrid[2])
    elif numbrid[0] == '5' or numbrid[0] == '6':
        aasta = ('20' + numbrid[1] + numbrid[2])
    kuu = (numbrid[3] + numbrid[4])
    if kuu == '01':
        kuu = 'jaanuar'
    elif kuu == '02':
        kuu = 'veebruar'
    elif kuu == '03':
        kuu = 'märts'
    elif kuu == '04':
        kuu = 'aprill'
    elif kuu == '05':
        kuu = 'mai'
    elif kuu == '06':
        kuu = 'juuni'
    elif kuu == '07':
        kuu = 'juuli'
    elif kuu == '08':
        kuu = 'august'
    elif kuu == '09':
        kuu = 'september'
    elif kuu == '10':
        kuu = 'oktoober'
    elif kuu == '11':
        kuu = 'november'
    elif kuu == '12':
        kuu = 'detsember'
    kuupäev = (numbrid[5] + numbrid[6])
    return (kuupäev + '. ' + kuu + ' ' + aasta)