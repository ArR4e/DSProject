#alustasin 13.10.2021 (20:11)
def sünnikuupäev(ikood):
    kuud = ['jaanuar', 'veebruar', 'märts', 'aprill', 'mai', 'juuni', 'juuli', 'august', 'september', 'oktoober', 'november', 'detsember']
    
    if ikood[0] == '1':
        aasta = ikood[1:3]
        kuu1 = ikood[3:5]
        kuu2 = kuud[int(kuu1) - 1]
        paev = ikood[5:7]
        sunnikuupaev = paev + '. ' + kuu2 + ' 18' + aasta 
        return sunnikuupaev
    
    if ikood[0] == '2':
        aasta = ikood[1:3]
        kuu1 = ikood[3:5]
        kuu2 = kuud[int(kuu1) - 1]
        paev = ikood[5:7]
        sunnikuupaev = paev + '. ' + kuu2 + ' 18' + aasta 
        return sunnikuupaev
    
    if ikood[0] == '3':
        aasta = ikood[1:3]
        kuu1 = ikood[3:5]
        kuu2 = kuud[int(kuu1) - 1]
        paev = ikood[5:7]
        sunnikuupaev = paev + '. ' + kuu2 + ' 19' + aasta
        return sunnikuupaev
    
    if ikood[0] == '4':
        aasta = ikood[1:3]
        kuu1 = ikood[3:5]
        kuu2 = kuud[int(kuu1) - 1]
        paev = ikood[5:7]
        sunnikuupaev = paev + '. ' + kuu2 + ' 19' + aasta
        return sunnikuupaev
    
    if ikood[0] == '5':
        aasta = ikood[1:3]
        kuu1 = ikood[3:5]
        kuu2 = kuud[int(kuu1) - 1]
        paev = ikood[5:7]
        sunnikuupaev = paev + '. ' + kuu2 + ' 20' + aasta
        return sunnikuupaev
    
    if ikood[0] == '6':
        aasta = ikood[1:3]
        kuu1 = ikood[3:5]
        kuu2 = kuud[int(kuu1) - 1]
        paev = ikood[5:7]
        sunnikuupaev = paev + '. ' + kuu2 + ' 20' + aasta
        return sunnikuupaev