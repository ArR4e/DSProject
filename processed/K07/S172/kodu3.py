def kuud(kuu):
    if kuu == '01':
        return ' jaanuar '
    elif kuu == '02':
        return ' veebruar '
    elif kuu == '03':
        return ' märts '
    elif kuu == '04':
        return ' aprill '
    elif kuu == '05':
        return ' mai '
    elif kuu == '06':
        return ' juuni '
    elif kuu == '07':
        return ' juuli '
    elif kuu == '08':
        return ' august '
    elif kuu == '09':
        return ' september '
    elif kuu == '10':
        return ' oktoober '
    elif kuu == '11':
        return ' november '
    elif kuu == '12':
        return ' detsember '
    
def aastad(aasta):
    if int(aasta) < 21:
        return '20' + aasta
    else:
        return '19' + aasta

def sünnikuupäev(isikukood):
    aasta_arv = isikukood[1] + isikukood[2]
    kuu_arv = isikukood[3] + isikukood[4]
    paeva_arv = isikukood[5] + isikukood[6]
    paev = paeva_arv + '.'
    kuu = kuud(kuu_arv)
    aasta = aastad(aasta_arv)
    kuupaev = paev + kuu + aasta
    return kuupaev
    