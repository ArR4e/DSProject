def sünnikuupäev(ik):
    c=(ik[0])
    aa=(ik[1:3])
    mm=(ik[3:5])
    dd=(ik[5:7])
    if c == '1' or c == '2':
        aaaa = '18' + aa
    if c == '3' or c == '4':
        aaaa='19'+aa
    if c =='5' or c =='6':
        aaaa ='20'+aa
    if mm =='01':
        kuu='jaanuar'
    elif mm =='02':
        kuu='veebruar'
    elif mm =='03':
        kuu='märts'
    elif mm =='04':
        kuu='aprill'
    elif mm =='05':
        kuu='mai'
    elif mm =='06':
        kuu='juuni'
    elif mm =='07':
        kuu='juuli'
    elif mm =='08':
        kuu='august'
    elif mm =='09':
        kuu='september'
    elif mm =='10':
        kuu='oktoober'
    elif mm =='11':
        kuu='november'
    else:
        kuu='detsember'
    return(str(dd+". "+ kuu +" " + aaaa))