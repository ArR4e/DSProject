def sünnikuupäev(isikukood):
    aastanr_lõpp = isikukood[1] + isikukood[2]
    kuu = int(isikukood[3] + (isikukood[4]))-1
    päev = isikukood[5] + isikukood[6]
    kuude_nimetused = ['jaanuar', 'veebruar', 'märts', 'aprill', 'mai', 'juuni', 'juuli', 'august', 'september', 'oktoober', 'november', 'detsember']
    
    if int(isikukood[0]) == '1' or int(isikukood[0]) == '2':
        sajand = '18'
    elif int(isikukood[0]) == '3' or int(isikukood[0]) == '4':
            sajand = '19'
    else:
        sajand = '20'
    aasta = sajand + aastanr_lõpp
    sünnikuupäev = päev + '. ' + kuude_nimetused[kuu] + ' ' + aasta
    return(sünnikuupäev)

print(sünnikuupäev('60211212742'))