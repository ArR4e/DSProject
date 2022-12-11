def sünnikuupäev(isikukood):
    aastaajad = ['jaanuar', 'veebruar', 'märts', 'aprill', 'mai', 'juuni', 'juuli', 'august', 'september', 'oktoober', 'november', 'detsember']
    kuupaev = isikukood[5:7]
    if isikukood[3] == '1':
        if isikukood[4] == '0':
            kuu = aastaajad[9]
        elif isikukood[4] == '1':
            kuu = aastaajad[10]
        elif isikukood[4] == '2':
            kuu = aastaajad[11]
    else:
        kuu = aastaajad[int(isikukood[4]) - 1]
        
    if isikukood[0] == '1' or isikukood[0] == '2':
        aasta = int(isikukood[1:3]) + 1800
    elif isikukood[0] == '3' or isikukood[0] == '4':
        aasta = int(isikukood[1:3]) + 1900
    elif isikukood[0] == '5' or isikukood[0] == '6':
        aasta = int(isikukood[1:3]) + 2000
    elif isikukood[0] == '7' or isikukood[0] == '8':
        aasta = int(isikukood[1:3]) + 2100
        
    return (' '.join((kuupaev + '.', kuu, str(aasta))))

isikukood = input('Sisestage oma isikukood: ')
print(sünnikuupäev(isikukood))
    
