def sünnikuupäev(id):
    kuud = ['jaanuar','veebruar','märts','aprill','mai','juuni','juuli','august','september','oktoober','november','detsember']
    if id[0] in '12':
        aasta = '18' + id[1:3]
    elif id[0] in '34':
        aasta = '19' + id[1:3]
    elif id[0] in '56':
        aasta = '20' + id[1:3]
    elif id[0] in '78':
        aasta = '21' + id[1:3]
    kuu = kuud[int(id[3:5])-1]
    päev = id[5:7]
    return päev + ". " + kuu + ' ' + aasta

