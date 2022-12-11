def sünnikuupäev(kood):
    aastad = ['18', '19', '20']
    kuud = ['jaanuar', 'veebruar', 'märts', 'aprill', 'mai', 'juuni', 'juuli', 'august', 'september', 'oktoober', 'november', 'detsember']
    kuu = kuud[int(kood[3] + kood[4]) - 1]
    aastad_1 = kood[1] + kood[2] 
    
    if kood[0] == '1' or kood[0] == '2':
        aasta = aastad[0] + aastad_1
    if kood[0] == '3' or kood[0] == '4':
        aasta = aastad[1] + aastad_1
    if kood[0] == '5' or kood[0] == '6':
        aasta = aastad[2] + aastad_1
    päev = kood[5] + kood[6]
    a = '{0}. {1} {2}'.format(päev, kuu, aasta)
    return a
print(sünnikuupäev('39910122345'))