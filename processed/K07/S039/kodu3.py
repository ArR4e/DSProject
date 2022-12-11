def sünnikuupäev(isikukood):
    sajand=isikukood[0]
    aasta=isikukood[1:3]
    kuu=isikukood[3:5]
    päev=isikukood[5:7]
    if sajand=='3' or sajand=='4':
        sajand=19
    elif sajand=='5' or sajand=='6':
        sajand=20
    elif sajand=='1' or sajand=='2':
        sajand=18
    õige_aasta=str(sajand)+str(aasta)
    if kuu=='01':
        kuu='jaanuar'
    elif kuu=='02':
        kuu='veebruar'
    elif kuu=='03':
        kuu='märts'
    elif kuu=='04':
        kuu='aprill'
    elif kuu=='05':
        kuu='mai'
    elif kuu=='06':
        kuu='juuni'
    elif kuu=='07':
        kuu='juuli'
    elif kuu=='08':
        kuu='august'
    elif kuu=='09':
        kuu='september'
    elif kuu=='10':
        kuu='oktoober'
    elif kuu=='11':
        kuu='november'
    elif kuu=='12':
        kuu='detsember'
    return päev+". "+kuu+" "+õige_aasta
print(sünnikuupäev('34501234215'))