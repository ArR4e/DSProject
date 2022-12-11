def sünnikuupäev(isikukood):
    kuud = {'01':'jaanuar',
            '02':'veebruar',
            '03':'märts',
            '04':'aprill',
            '05':'mai',
            '06':'juuni',
            '07':'juuli',
            '08':'august',
            '09':'september',
            '10':'oktoober',
            '11':'november',
            '12':'detsember'}
    
    if isikukood[0] in ('1', '2'): aasta = '18'+isikukood[1:3]
    elif isikukood[0] in ('3', '4'): aasta = '19'+isikukood[1:3]
    elif isikukood[0] in ('5', '6'): aasta = '20'+isikukood[1:3]
    
    kuu = kuud[isikukood[3:5]]
    päev = isikukood[5:7]
    
    return f'{päev}. {kuu} {aasta}'
