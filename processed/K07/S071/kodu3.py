# võtab argumendiks Eesti isikukoodi sõnena ning tagastab sünnikuupäeva kujul <päev>. <kuu nimi> <aasta>
def sünnikuupäev(number):
    eraldatud = []
    for i in number:
        eraldatud.append(i)
    print(eraldatud)
    
    # päeva tegemine
    päev = str(eraldatud[5]) + str(eraldatud[6]) + ". "
    
    # kuu leidmine
    kuud = ['jaanuar','veebruar','märts','aprill','mai','juuni','juuli','august','september','oktoober','november','detsember']
    kuu2 = str(eraldatud[3]) + str(eraldatud[4])
    if eraldatud[3] == 0:
        kuu = kuud[eraldatud[3] - 1] + " "
    else:
        kuu = kuud[int(eraldatud[3] + eraldatud[4]) - 1] + " "
    
    
    # aasta kokkupanek
    if eraldatud[0] == "5" or eraldatud[0] == "6":
        aasta = "20" + str(eraldatud[1]) + str(eraldatud[2])
    elif eraldatud[0] == "3" or eraldatud[0] == "4":
        aasta = "19" + str(eraldatud[1]) + str(eraldatud[2])
    else:
        aasta = "18" + str(eraldatud[1]) + str(eraldatud[2])
    
    lause = päev + kuu + aasta
    return lause

print(sünnikuupäev("60209196012"))