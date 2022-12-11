def sünnikuupäev(isikukood):
    mu_list = []
    x = 0
    for i in isikukood:
        mu_list.append(i)
        x = x + 1
    kuu = mu_list[3] + mu_list[4]
    päev = mu_list[5] + mu_list[6]
    aasta = mu_list[1] + mu_list[2]
    if mu_list[0]== '1' or mu_list[0]== '2':
        aasta= '18' + aasta
    elif mu_list[0]== '3' or mu_list[0]== '4':
        aasta = '19' + aasta
    elif mu_list[0] == '5' or mu_list[0]== '6':
        aasta = '20' + aasta
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
    kogu = päev + '. ' + kuu + ' ' + aasta
    return kogu
x = sünnikuupäev('44501234215')
print(x)
