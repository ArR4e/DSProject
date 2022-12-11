kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
def sünnikuupäev(isikukood):
    aasta_esimene_pool = ""
    if isikukood[0] == "3" or isikukood[0] == "4":
        aasta_esimene_pool = "19"
    if isikukood[0] == "1" or isikukood[0] == "2":
        aasta_esimene_pool = "18"
    if isikukood[0] == "5" or isikukood[0] == "6":
        aasta_esimene_pool = "20"
    if isikukood[0] == "7" or isikukood[0] == "8":
        aasta_esimene_pool = "21"

        
    aasta_teine_pool = isikukood[1:3]
    kogu_aasta = aasta_esimene_pool + aasta_teine_pool
    str_kuu = isikukood[3:5]
    kuu_number = 0
    if str_kuu[0] == "0":
        kuu_number = int(str_kuu[1])
    else:
        kuu_number = int(str_kuu)
    
    tagasta_kuu = kuud[kuu_number-1]
    
    str_paev = isikukood[5:7]
    paev_number = 0
    if str_paev[0] == "0":
        paev_number = int(str_paev[1])
    else:
        paev_number = int(str_paev)
    
    return str(paev_number) + ". " + tagasta_kuu + " " + kogu_aasta
    
    
print(sünnikuupäev('34501234215'))
        
    