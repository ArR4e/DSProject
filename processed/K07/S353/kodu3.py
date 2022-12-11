def sünnikuupäev(sõne):
    aastasõne=''
    if sõne[0]=='2' or sõne[0]=='1':
        aastasõne+='18'
    elif sõne[0]=='3' or sõne[0]=='4':
        aastasõne+='19'
    elif sõne[0]=='5' or sõne[0]=='6':
        aastasõne+='20'
    aastasõne+=sõne[1]+sõne[2]
    if sõne[3:5]=='01':
        kuusõne='jaanuar'
    elif sõne[3:5]=='02':
        kuusõne='veebruar'
    elif sõne[3:5]=='03':
        kuusõne='märts'
    elif sõne[3:5]=='04':
        kuusõne='aprill'
    elif sõne[3:5]=='05':
        kuusõne='mai'
    elif sõne[3:5]=='06':
        kuusõne='juuni'
    elif sõne[3:5]=='07':
        kuusõne='juuli'
    elif sõne[3:5]=='08':
        kuusõne='august'
    elif sõne[3:5]=='09':
        kuusõne='september'
    elif sõne[3:5]=='10':
        kuusõne='oktoober'
    elif sõne[3:5]=='11':
        kuusõne='november'
    elif sõne[3:5]=='12':
        kuusõne='detsember'
    päevasõne=sõne[5:7]
    sünnikuupäevasõne=päevasõne+'. '+kuusõne+' '+aastasõne
    return sünnikuupäevasõne
    