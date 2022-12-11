def sünnikuupäev(isikukood):
    kuud = ['jaanuar', 'veebruar', 'märts', 'aprill',
                  'mai', 'juuni', 'juuli', 'august', 'september',
                  'oktoober', 'november', 'detsember']
    päev = isikukood[5:7]
    kuu = kuud[int(isikukood[3:5])-1]
    sajand = isikukood[0:1]
    aasta = isikukood[1:3]
    
    if sajand == '1' or sajand == '2':
        sajand = '18'
    elif sajand == '3' or sajand == '4':
        sajand = '19'
    elif sajand == '5' or sajand == '6':
        sajand = '20'
    elif sajand == '7' or sajand == '8':
        sajand = '21'
        
    

    return(päev+'.'+' '+kuu+' '+sajand + aasta)
