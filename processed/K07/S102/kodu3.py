def sünnikuupäev(kood):
    if int(kood[0])<=2:
       aasta='18'+kood[1:3]
    elif int(kood[0])<=4:
        aasta='19'+kood[1:3]
    else:
        aasta='20'+kood[1:3]
    kuu=['jaanuar','veebruar','märts','aprill','mai','juuni','juuli','august','september','oktoober','november','detsember']
    if kood[3]=='0':
        a=int(kood[4])-1
    else:
        a=int(kood[3:5])-1
    if kood[5]=='0':
        return kood[6]+'. '+kuu[a]+' '+aasta
    else:   
        return kood[5:7]+'. '+kuu[a]+' '+aasta


    