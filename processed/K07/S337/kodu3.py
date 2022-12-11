def sünnikuupäev(kood):
    aasta = kood[1:3]
    kuu = int(kood[3:5])
    päev = str(kood[5:7])
    kuud = ['jaanuar', 'veebruar', 'märts', 'aprill', 'mai', 'juuni', 'juuli', 'august', 'september', 'oktoober', 'november', 'detsember']
    kuu = kuud[kuu-1]
    if int(kood[0]) == 1 or int(kood[0]) ==  2:
        aasta = '18'+str(aasta)
    elif int(kood[0]) == 3 or int(kood[0]) == 4:
        aasta = '19'+str(aasta)
    else:
        aasta = '20'+str(aasta)
    kuupäev = päev+'. '+kuu +' '+ aasta
    return str(kuupäev)
sünnikuupäev('39910122345')