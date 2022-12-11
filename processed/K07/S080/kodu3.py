def sünnikuupäev(isikukood):
    a = isikukood[1:3]
    b = isikukood[3:5]
    c = isikukood[5:7]
    d = isikukood[0]
    if int(d) <= 2:
        aasta = 1800 + int(a)
        aasta = str(aasta)
    elif int(d)>2 and int(d)<=4:
        aasta = 1900 + int(a)
        aasta = str(aasta)
    else:
        aasta = 2000 + int(a)
        aasta = str(aasta)
    #if int(a) >= 00 and int(a) <= 21:
        #aasta = 2000 + int(a)
        #aasta = str(aasta)
    #else:
        #aasta = 1900 + int(a)
        #aasta = str(aasta)
    if b == '01':
        kuu = 'jaanuar'
    elif b == '02':
        kuu = 'veebruar'
    elif b == '03':
        kuu = 'märts'
    elif b == '04':
        kuu = 'aprill'
    elif b == '05':
        kuu = 'mai'
    elif b == '06':
        kuu = 'juuni'
    elif b == '07':
        kuu = 'juuli'
    elif b == '08':
        kuu = 'august'
    elif b == '09':
        kuu = 'september'
    elif b == '10':
        kuu = 'oktoober'
    elif b == '11':
        kuu = 'november'
    else:
        kuu = 'detsember'
    #päev = int(c)
    #päev = str(päev)
    päev = c
    return(päev+'. '+kuu+' '+aasta)
    
sünnikuupäev(str(55505055555))