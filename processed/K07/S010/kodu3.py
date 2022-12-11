def sünnikuupäev(isikukood):
    sajand=isikukood[0]
    aasta=isikukood[1:3]
    if sajand=='1' or sajand=='2':
        aasta='18'+aasta
    if sajand=='3' or sajand=='4':
        aasta='19'+aasta
    if sajand=='5' or sajand=='6':
        aasta='20'+aasta
    if sajand=='7' or sajand=='8':
        aasta='21'+aasta
    kuu=isikukood[3:5]
    if kuu=='01':
        ks='jaanuar'
    if kuu=='02':
        ks='veebruar'
    if kuu=='03':
        ks='märts'
    if kuu=='04':
        ks='aprill'
    if kuu=='05':
        ks='mai'
    if kuu=='06':
        ks='juuni'
    if kuu=='07':
        ks='juuli'
    if kuu=='08':
        ks='august'
    if kuu=='09':
        ks='september'
    if kuu=='10':
        ks='oktoober'
    if kuu=='11':
        ks='november'
    if kuu=='12':
        ks='detsember'
    päev=isikukood[5:7]
    if isikukood[5]=='0':
        päev=isikukood[6:7]
    lause=päev+'.'+' '+ks+' '+aasta
    return lause
    
print(sünnikuupäev('34501234215'))