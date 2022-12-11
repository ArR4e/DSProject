def sünnikuupäev(isikukood):
    if len(isikukood) < 11 or len(isikukood) >= 12:
        return 'Error: length not 11'
    
    sünnikuupäev = ''
    
    if int(isikukood[5:7]) < 32:
        sünnikuupäev += str(isikukood[5:7] + '. ')
    else:
        return "bigerror: vigane isikukood"
    
    
    if isikukood[3:5] == '01':
        sünnikuupäev += 'jaanuar'
    elif isikukood[3:5] == '02':
        sünnikuupäev += 'veebruar'
    elif isikukood[3:5] == '03':
        sünnikuupäev += 'märts'
    elif isikukood[3:5] == '04':
        sünnikuupäev += 'aprill'
    elif isikukood[3:5] == '05':
        sünnikuupäev += 'mai'
    elif isikukood[3:5] == '06':
        sünnikuupäev += 'juuni'
    elif isikukood[3:5] == '07':
        sünnikuupäev += 'juuli'
    elif isikukood[3:5] == '08':
        sünnikuupäev += 'august'
    elif isikukood[3:5] == '09':
        sünnikuupäev += 'september'
    elif isikukood[3:5] == '10':
        sünnikuupäev += 'oktoober'
    elif isikukood[3:5] == '11':
        sünnikuupäev += 'november'
    elif isikukood[3:5] == '12':
        sünnikuupäev += 'detsember'
    else:
        return 'Error: Vigane isikukood'
    
    if isikukood[0] in ('3','4'):
        sünnikuupäev += ' 19'+ str(isikukood[1:3])
    elif isikukood[0] in ('1','2'):
        sünnikuupäev += ' 18' + str(isikukood[1:3])
    else:
        sünnikuupäev += ' 20' + str(isikukood[1:3])
        
        
    return sünnikuupäev


