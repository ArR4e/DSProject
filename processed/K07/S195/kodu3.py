def sajandf(x):
    if x == '3' or x == '4':
        return int(1900)
    elif x == '5' or x == '6':
        return int(2000)
    print("See ei eksisteeri isikukoodina.")
    
def kuuf(x):
    if x == '01':
        return 'Jaanuar'
    elif x == '02':
        return 'Veebruar'
    elif x == '03':
        return 'Märts'
    elif x == '04':
        return 'Aprill'
    elif x == '05':
        return 'Mai'
    elif x == '06':
        return 'Juuni'
    elif x == '07':
        return 'Juuli'
    elif x == '08':
        return 'August'
    elif x == '09':
        return 'September'
    elif x == '10':
        return 'Oktoober'
    elif x == '11':
        return 'November'
    elif x == '12':
        return 'Detsember'
    
def sünnikuupäev(x):
    aasta = 0
    x = str(x)
    y = list(x)
    aastal6pp = "".join(y[1:3])
    aasta = sajandf(y[0])
    aasta += int(aastal6pp)
    kuu = kuuf("".join(y[3:5]))
    p2ev = ''.join(y[5:7])
    #print(p2ev+'.',kuu,aasta)
    m = (p2ev+'.',kuu,str(aasta))
    return ' '.join(m)