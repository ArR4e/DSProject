def  sünnikuupäev (ik):
    kuud = ['jaanuar', 'veebruar', 'märts', 'aprill', 'mai','juuni','juuli', 'august','september', 'oktoober','november','detsember']
    
    kp = ik[5:7]
    kuu = ik[3:5]
    
    if kuu == '10':
        kuu = int(kuu)
    else:
        kuu = int(kuu.strip('0'))
        
    aasta = ik[1:3]
    
    if ik[0] == '5' or ik[0] == '6':
        aasta = '20'+aasta
        
    elif ik[0] == '3' or ik[0] == '4':
        aasta = '19'+aasta
        
    else:
        aasta = '18'+aasta
    
    return (kp+'. '+kuud[kuu-1]+' '+aasta)

print(sünnikuupäev('39809016938'))

