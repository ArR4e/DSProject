def kuu(y):
    if y == '01':
        return 'jaanuar'
    elif y == '02':
        return 'veebruar'
    elif y == '03':
        return 'märts'
    elif y == '04':
        return 'aprill'
    elif y == '05':
        return 'mai'
    elif y == '06':
        return 'juuni'
    elif y == '07':
        return 'juuli'
    elif y == '08':
        return 'august'
    elif y == '09':
        return 'september'
    elif y == '10':
        return 'oktoober'
    elif y == '11':
        return 'november'
    elif y == '12':
        return 'detsember'
    
def sünnikuupäev(x):
    päev = x[5:7]
    k = kuu(x[3:5])
    if x[0] == '1' or x[0] == '2':
        aasta = '18' + x[1:3]
    elif x[0] == '3' or x[0] == '4':
        aasta = '19' + x[1:3]
    elif x[0] == '5' or x[0] == '6':
        aasta = '20' + x[1:3]
    return str(päev) + '. ' + k + ' ' + str(aasta)

    