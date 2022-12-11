def sünnikuupäev(idkood):
    paev = int(idkood[5:7])
    kuud = ['jaanuar','veebruar','märts','aprill','mai','juuni','juuli','august','september','oktoober','november','detsember']
    kuu = kuud[int(idkood[3:5])-1]
    temp = idkood[1:3]
    if int(idkood[0]) in [1,2]:
        aasta = "18"
    elif int(idkood[0]) in [3,4]:
        aasta = "19"
    else:
        aasta = "20"
    aasta += temp
    
    return f"{paev}. {kuu} {aasta}"