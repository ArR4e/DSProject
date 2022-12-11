x = str(input('Sisesta isikukood'))


def sünnikuupäev(x):
    päev = x[5:7]
    kuu = x[3:5]
    print(kuu)
    if kuu == '01':
        kuu = 'jaanuar'
    if kuu == '02':
        kuu = 'veebruar'
    if kuu == '03':
        kuu = 'märts'
    if kuu == '04':
        kuu = 'april'
    if kuu == '05':
        kuu = 'mai'
    if kuu == '06':
        kuu = 'juuni'
    if kuu == '07':
        kuu = 'juuli'
    if kuu == '08':
        kuu = 'august'
    if kuu == '09':
        kuu = 'september'
    if kuu == '10':
        kuu = 'oktoober'
    if kuu == '11':
        kuu = 'november'
    if kuu == '12':
        kuu = 'detsember'

    
    
    
    
    aasta1 = x[1:3]
    if x[0] == '1' or '2':
        aasta = '18' + aasta1
    if x[0] == '3' or '4':
        aasta = '19' + aasta1
    if x[0] == '5' or '6':
        aasta = '20' + aasta1
    print(päev + '. ' + kuu + ' ' + aasta)
    
sünnikuupäev(x)