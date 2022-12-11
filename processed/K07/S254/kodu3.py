def sünnikuupäev(isikukood):
    aasta = isikukood[1:3]
    kuu = isikukood[3:5]
    päev = str(isikukood[5:7])
    
    kuud = ['jaanuar', 'veebruar', 'märts', 'aprill', 'mai', 'juuni', 'juuli', 'august', 'september', 'oktoober', 'november', 'detsember']
    kuu_sõnana = kuud[int(kuu)-1]
    
    arvutatud_aasta = ''
    if int(isikukood[0]) == 1 or int(isikukood[0]) == 2:
        arvutatud_aasta = '18' + str(aasta)
    elif  int(isikukood[0]) == 3 or int(isikukood[0]) == 4:
        arvutatud_aasta = '19' + str(aasta)
    elif  int(isikukood[0]) == 5 or int(isikukood[0]) == 6:
        arvutatud_aasta = '20' + str(aasta)
    
    sünnipäev = str(päev) + '. ' + str(kuu_sõnana) + ' ' + arvutatud_aasta
    return (sünnipäev)



print(sünnikuupäev('39901124215'))