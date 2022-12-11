def sünnikuupäev(isikukood):
    
    järjend = [int(x) for x in str(isikukood)]
    aasta_num = järjend(range(1, 3))
    aasta = "".join([aasta_num])
    kuu_num = järjend(range(3, 5))
    kuu = "".join([kuu_num])
    päev_num = järjend(range(5,7))
    päev = "".join([päev_num])
    if kuu == 1:
        kuu = Jaanuar
    elif kuu == 2:
        kuu = Veebruar
    elif kuu == 3:
        kuu = Märts
    elif kuu == 4:
        kuu = Aprill
    elif kuu == 5:
        kuu = Mai
    elif kuu == 6:
        kuu = Juuni
    elif kuu == 7:
        kuu = Juuli
    elif kuu == 8:
        kuu = August
    elif kuu == 9:
        kuu = September
    elif kuu == 10:
        kuu = Oktoober
    elif kuu == 11:
        kuu = November
    elif kuu == 12:
        kuu = Detsember
    print(kuu)
    
sünnikuupäev(49610250276)

#Küll ma tunnis küsin siis, ei saa päris täpselt aru