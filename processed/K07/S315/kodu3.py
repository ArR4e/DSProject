def sünnikuupäev(isikukood):
    päev = isikukood[5:7]
    kuu = isikukood[3:5]
    aasta = isikukood[1:3]
    sajand = isikukood[0]
    
    if päev[0] == 0:
        päev = päev[1]
    if kuu == '01':
        kuu = "jaanuar"
    elif kuu == '02':
        kuu = "veebruar"
    elif kuu == '03':
        kuu = "märts"
    elif kuu == '04':
        kuu = "aprill"
    elif kuu == '05':
        kuu = "mai"
    elif kuu == '06':
        kuu = "juuni"
    elif kuu == '07':
        kuu = "juuli"
    elif kuu == '08':
        kuu = "august"
    elif kuu == '09':
        kuu = "september"
    elif kuu == '10':
        kuu = "oktoober"
    elif kuu == '11':
        kuu = "november"
    elif kuu == '12':
        kuu = "detsember"
    if sajand == '1' or sajand == '2':
        aasta = '18' + aasta
    elif sajand == '3' or sajand == '4':
        aasta = '19' + aasta
    elif sajand == '5' or sajand == '6':
        aasta = '20' + aasta
    return (f"{päev}. {kuu} {aasta}")
        