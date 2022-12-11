def sünnikuupäev(isikukood):
    kuud=['jaanuar','veebruar','märts','aprill','mai','juuni','juuli','august','september','oktoober','november','detsember']
    tagasi=''
    kuu=isikukood[3:5]
    päev=isikukood[5:7]
    aasta1=isikukood[0]
    aasta2=isikukood[1:3]
    if aasta1=='1' or aasta1=='2':
        aasta1='18'
    if aasta1=='3' or aasta1=='4':
        aasta1='19'
    if aasta1=='5' or aasta1=='6':
        aasta1='20'
    if aasta1=='7' or aasta1=='8':
        aasta1='21'
    kuu=kuud[int(kuu)-1]
    tagasi+=päev+'. '+kuu+' '+aasta1+aasta2
    return(tagasi)