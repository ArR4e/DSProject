isikukood = input("Sisestage oma isikukood: ")

def sünnikuupäev(isikukood):
    aasta = isikukood[1:3]
    kuu = isikukood[3:5]
    päev = isikukood[5:7]
    if isikukood[0] == '5' or isikukood[0] == '6':
        aasta = '20' + aasta
    if isikukood[0] == '3' or isikukood[0] == '4':
        aasta = '19' + aasta
    if isikukood[0] == '1' or isikukood[0] == '2':
        aasta = '18' + aasta
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
    return päev + '. ' + kuu + ' ' + aasta

print(sünnikuupäev(isikukood))
    