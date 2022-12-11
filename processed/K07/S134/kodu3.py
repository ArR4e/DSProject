def sünnikuupäev(ik):
    x = [int(a) for a in str(ik)]
    aasta = "".join(x[1, 2])
    if aasta < 21:
        a = 2000 + aasta
    else:
        a = 1900 + aasta
    kuu = "".join(x[3, 4])
    if kuu == 01:
        k = "jaanuar"
    elif kuu == 02:
        k = "veebruar"
    elif kuu == 03:
        k = "märts"
    elif kuu == 04:
        k = "aprill"
    elif kuu == 05:
        k = "mai"
    elif kuu == 06:
        k = "juuni"
    elif kuu == 07:
        k = "juuli"
    elif kuu == 08:
        k = "august"
    elif kuu == 09:
        k = "september"
    elif kuu == 10:
        k = "oktoober"
    elif kuu == 11:
        k = "november"
    elif kuu == 12:
        k = "detsember"
    kuupäev = join.x[5, 6]
    return(str(kuupäev)+"."+str(k)+str(a))

sünnikuupäev(50202160276)