def sünnikuupäev(ik):
    ik = str(ik)
    kuud = ('jaanuar','veebruar','märts','aprill','mai','juuni','juuli','august','september','oktoober','november','detsember')
    kuu = int(ik[3:5])
    aasta = int(ik[1:3])
    kuupaev = int(ik[5:7])
    if int(ik[0]) <=2:
        aasta = aasta +1800
    elif int(ik[1]) ==5:
        aasta = aasta +2000
    elif aasta > 18:
       aasta = aasta+1900
    elif aasta < 18:
       aasta = aasta+2000
    a =(str(kuupaev),". ",str(kuud[kuu-1])," ",str(aasta))
    return("".join(a))
    