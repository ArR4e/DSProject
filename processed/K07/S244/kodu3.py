def sünnikuupäev(isikukood):
    kuude_järjend = ['jaanuar', 'veebruar', 'märts', 'aprill', 'mai', 'juuni', 'juuli', 'august', 'september', 'oktoober', 'november', 'detsember']
    kuu = kuude_järjend[int(isikukood[3:5])-1]
    päev = int(isikukood[5:7])
    if int(isikukood[0]) == 1 or int(isikukood[0]) == 2:
        aasta = int('18' + isikukood[1:3])
        return str(päev) + '. ' + str(kuu) + ' ' + str(aasta)
    elif int(isikukood[0]) == 3 or int(isikukood[0]) == 4:
        aasta = int('19' + isikukood[1:3])
        return str(päev) + '. ' + str(kuu) + ' ' + str(aasta)
    elif int(isikukood[0]) == 5 or int(isikukood[0]) == 6:
        aasta = int('20' + isikukood[1:3])
        return str(päev) + '. ' + str(kuu) + ' ' + str(aasta)
    elif int(isikukood[0]) == 7 or int(isikukood[0]) == 8:
        aasta = int('21' + isikukood[1:3])
        return str(päev) + '. ' + str(kuu) + ' ' + str(aasta)

        
    
isikukood = input('Sisesta iskukood: ')
print(sünnikuupäev(isikukood))