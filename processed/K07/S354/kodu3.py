#34501234215
def sünnikuupäev(b):
    a = str(b)
    try:
        a = str(b)
        g = a[1] + a[2]
        k = a[3] + a[4]
        d = a[5] + a[6]
        if int(g) >= 22:
            g = '19' + g
        else:
            g = '20' + g
            
        if k == '01':
            k = 'jaanuar'
        if k == '02':
            k = 'veebruar'
        if k == '03':
            k = 'märts'
        if k == '04':
            k = 'aprill'
        if k == '05':
            k = 'mai'
        if k == '06':
            k = 'juuni'
        if k == '07':
            k = 'juuli'
        if k == '08':
            k = 'august'
        if k == '09':
            k = 'september'
        if k == '10':
            k = 'oktoober'
        if k == '11':
            k = 'november'
        if k == '12':
            k = 'detsember'
        if int(a[5]) == 0:
            d = a[6]
        return (d + '. ' + k + ' ' + g)
    except:
        return 0