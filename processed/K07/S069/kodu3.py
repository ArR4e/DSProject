def sünnikuupäev(isikukood):
    isikukood = str(isikukood)
    jarjend = list(isikukood)
    päev = jarjend[5], jarjend[6], '.'
    päev = str(''.join(päev))
    kuu = jarjend[3], jarjend[4]
    if int(jarjend[3]) > 0:
        kuu = int(''.join(kuu))
    else:
        kuu = int(jarjend[4])
    kuud = ['jaanuar', 'veebruar', 'märts', 'aprill', 'mai', 'juuni', 'juuli', 'august', 'september', 'oktoober', 'november', 'detsember']
    if int(jarjend[0]) == 5 or int(jarjend[0]) == 6:
        aasta = jarjend[1], jarjend[2]
        if int(jarjend[1]) > 0:
            aasta = int(''.join(aasta))
        else:
            aasta = int(jarjend[2])
        sünniaasta = 2000 + aasta
    else:
        aasta = jarjend[1], jarjend[2]
        if int(jarjend[1]) > 0:
            aasta = int(''.join(aasta))
        else:
            aasta = int(jarjend[2])
        sünniaasta = 1900 + aasta
          
    vastus = str(päev+' '+kuud[kuu-1]+' '+str(sünniaasta))
    return vastus
    
    
    

    