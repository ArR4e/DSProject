#Sünnikuupäev

def sünnikuupäev(isikukood):
    isikukood = str(isikukood)
    kuud = ('jaanuar', 'veebruar', 'märts', 'aprill', 'mai', 'juuni', 'juuli', 'august', 'september', 'oktoober', 'november', 'detsember')
    if isikukood[0] == '1' or isikukood[0] == '2':
        aasta = 1800 + int(isikukood[1:3])
    elif isikukood[0] == '3' or isikukood[0] == '4':
        aasta = 1900 + int(isikukood[1:3])
    elif isikukood[0] == '5' or isikukood[0] == '6':
        aasta = 2000 + int(isikukood[1:3])
    elif isikukood[0] == '7' or isikukood[0] == '8':
        aasta = 2100 + int(isikukood[1:3])
        
    return str(isikukood[5:7]) + '. ' + kuud[int(isikukood[3:5])-1] + ' ' + str(aasta)