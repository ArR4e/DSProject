def sünnikuupäev(ikood):
    aasta=paev=kuu=''    
    kuud=['','jaanuar','veebruar','märts', 'aprill', 'mai', 'juuni', 'juuli', 'august', 'september', 'oktoober', 'november','detsember']
    
    if int(ikood[0])==3 or int(ikood[0])==4:
        aasta+='19'
    elif int(ikood[0])==5 or int(ikood[0])==6:
        aasta+='20'
    elif int(ikood[0])==1 or int(ikood[0])==2:
        aasta+='18'
    
    aasta+=ikood[1]+ikood[2]
    
    kuu=kuud[int(''.join(ikood[3:5]))]
    
    paev=''.join(ikood[5:7])
    
    return (paev+'. '+kuu+' '+aasta)
    
ikood=input('Sisesta isikukood: ')

sünnikuupäev(ikood)

