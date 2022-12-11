def sünnikuupäev(kood):
    a = kood[5] + kood[6]
    b = kood[3] + kood[4]
    if b == '01':
        b = 'jaanuar'
    elif b == '02':
        b = 'veebruar'
    elif b == '03':
        b = 'märts'
    elif b == '04':
        b = 'aprill'
    elif b == '05':
        b = 'mai'
    elif b == '06':
        b = 'juuni'
    elif b == '07':
        b = 'juuli'
    elif b == '08':
        b = 'august'
    elif b == '09':
        b = 'september'
    elif b == '10':
        b = 'oktoober'
    elif b == '11':
        b = 'november'
    elif b == '12':
        b = 'detsember'

    if kood[0] == '1' or kood[0] == '2':
        c = '18' + kood[1] + kood[2]
    elif kood[0] == '3' or kood[0] == '4':
        c = '19' + kood[1] + kood[2]
    elif kood[0] == '5' or kood[0] == '6':
        c = '20' + kood[1] + kood[2]
    elif kood[0] == '7' or kood[0] == '8':
        c = '21' + kood[1] + kood[2]
        
    return(a + '. ' + b + ' ' + c)

sünnikuupäev('50106251441')