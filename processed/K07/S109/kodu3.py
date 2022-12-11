def sünnikuupäev(x):
    päev = x[5:7]
    kuu = x[3:5]
    aasta = x[1:3]
    
    if int(kuu) == 1:
        k = 'jaanuar'
    elif int(kuu) == 2:
        k = 'veebruar'
    elif int(kuu) == 3:
        k = 'märts'
    elif int(kuu) == 4:
        k = 'aprill'
    elif int(kuu) == 5:
        k = 'mai'
    elif int(kuu) == 6:
        k = 'juuni'
    elif int(kuu) == 7:
        k = 'juuli'
    elif int(kuu) == 8:
        k = 'august'
    elif int(kuu) == 9:
        k = 'september'
    elif int(kuu) == 10:
        k = 'oktoober'
    elif int(kuu) == 11:
        k = 'november'
    else:
        k = 'detsember'
    
    if int(aasta) <= 21:
        s = 2000 + int(aasta)
    else:
        s = 1900 + int(aasta)
        
    print(päev + '.', k, s)