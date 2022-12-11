id = input("Sisesta isikukood: ")
isik = list(id)


def sünnikuupäev(id):
    kuu = 0
    kuupäev = 0
    a = 0
    b = 0
    kuupäev = str(id[5] + id[6]) + '. '
    
    if id[3] + id[4] == "01":
        kuu = "jaanuar "
    if id[3] + id[4] == "02":
        kuu = "veebruar "
    if id[3] + id[4] == "03":
        kuu = "märts "
    if id[3] + id[4] == "04":
        kuu = "aprill "
    if id[3] + id[4] == "05":
        kuu = "mai "
    if id[3] + id[4] == "06":
        kuu = "juuni "
    if id[3] + id[4] == "07":
        kuu = "juuli "
    if id[3] + id[4] == "08":
        kuu = "august "
    if id[3] + id[4] == "09":
        kuu = "september "
    if id[3] + id[4] == "10":
        kuu = "oktoober "
    if id[3] + id[4] == "11":
        kuu = "november "
    if id[3] + id[4] == "12":
        kuu = "detsember "

    if id[0] == "1" or id[0] == "2":
        a = str(int(id[1] + id[2])+ 1800)    
        
    if id[0] == "5" or id[0] == "6":
        a = str(int(id[1] + id[2])+ 2000)
        
    if id[0] == "4" or id[0] == "3":
        a = str(int(id[1] + id[2])+ 1900)

    
    return kuupäev + kuu + a

print(sünnikuupäev(id))
