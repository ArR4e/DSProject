#Sünnikuupäev isikukoodist

def sünnikuupäev(isik):
    # slice list sobivateks lõikudeks
    x = isik[1:7]
    kp = x[-2:]
    kuu = x[2:4]
    aasta = x[0:2]
    
    #eemaldab nulli 01, 02 jne kuude numbite eest
    if kuu[0] == "0":
        kuu = kuu[1]
        
    #1,2 == aastasada 1800, 3,4 == 1900, 5,6 == 2000    
    if int(isik[0]) == 1 or int(isik[0]) == 2:
        aasta = f'18{aasta}'
    elif int(isik[0]) == 3 or int(isik[0]) == 4:
        aasta = f'19{aasta}'
    elif int(isik[0]) == 5 or int(isik[0]) == 6:
        aasta = f'20{aasta}'
        
    #nullkuud pole olemas   
    kuud = ['null', 'jaanuar', 'veebruar', 'märts',
            'aprill', 'mai', 'juuni', 'juuli', 'august',
            'september', 'oktoober', 'november', 'detsember']
    
    #tagastab lõppväärtuse
    return f'{kp}. {kuud[int(kuu)]} {aasta}'
    
print(sünnikuupäev("34501234215"))