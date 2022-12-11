def sünnikuupäev(isikukood):
    arv = list(isikukood)
    kuupäev = ''.join(arv[5:7]) + '.'
    kuud = ['jaanuar', 'veebruar', 'märts', 'aprill', 'mai', 'juuni', 'juuli', 'august', 'september', 'oktoober', 'november', 'detsember']
    kuu = kuud[int(''.join(arv[3:5])) - 1]
    sajand = ['18', '18', '18', '19', '19', '20', '20']
    aasta = sajand[int(''.join(arv[0:1]))] + ''.join(arv[1:3])
    return(kuupäev + '' + kuu + ' ' + aasta)
