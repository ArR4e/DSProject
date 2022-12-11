def sünnikuupäev(kood):
    aasta=''
    paev=''
    kuu=''
    kuud=['jaanuar','veebruar','märts','aprill','mai','juuni','juuli','august','september','oktoober','november','detsember']
    if kood[0]=='5':
        aasta+='20'
    elif kood[0]=='6':
        aasta+='20'
    elif kood[0]=='4':
        aasta+='19'
    elif kood[0]=='3':
        aasta+='19'
    else:
        aasta+='18'
    aasta+=kood[1:3]
    paev+=kood[5:7]
    arv=kood[3]+kood[4]
    kuu=kuud[int(arv)-1]
    return str(paev+'. '+kuu+' '+aasta)