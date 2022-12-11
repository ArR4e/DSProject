def sünnikuupäev(isikukood):
    s = isikukood[0]
    a = isikukood[1:3]
    k = isikukood[3:5]
    p = isikukood[5:7]
    
    a = str(sajand(int(s))) + a
    if k[0] == '0': k=k[1]
    kuu_nimi = mis_kuu(int(k))
    if p[0] == '0': p=p[1]
        
    return str(p) + '. ' + str(kuu_nimi) +' '+ str(a)
    
def sajand(n):
    if n < 3:
        sajand = 18
    elif n < 5:
        sajand = 19
    elif n < 7:
        sajand = 20
    return sajand
    
    
def mis_kuu(kuu):
    if kuu <= 6:
        if kuu <= 3:
            if kuu < 2:
                nimi = "jaanuar"
            elif kuu> 2:
                nimi = "märts"
            else:
                nimi = "veebruar"
        else:
            if kuu < 5:
                nimi = "aprill"
            elif kuu> 5:
                nimi = "juuni"
            else:
                nimi = "mai"
    elif kuu <=12:
        if kuu <= 9:
            if kuu < 8:
                nimi = "juuli"
            elif kuu > 8:
                nimi = "september"
            else:
                nimi ="august"
        else:
            if kuu < 11:
                nimi = "oktoober"
            elif kuu> 11:
                nimi = "detsember"
            else:
                nimi ="november"
    return nimi
    
print(sünnikuupäev('34501034215'))
#print(mis_kuu(04))