def sünnikuupäev(isikukood):
    kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    sajandid = ["12 18", "34 19", "56 20", "78 21"]
    
    paev = isikukood[5:7].lstrip("0")
    
    # kuu: võtan isikukoodist need kaks numbrit, mis näitavad kuud, eemaldan
    # eespoolse nulli, lahutan sellest ühe ja sellega leian kuu nime kuude listist
    kuu = kuud[int((isikukood[3:5]).lstrip("0")) - 1]
    
    # aasta: võtan isikukoodi esimese numbri, mis näitab, mis sajandis aasta on,
    # ning sellega võtan sajandid listist õige väärtuse
    aasta = ""
    for sajand in sajandid:
        foo = sajand.split()
        if isikukood[0] in foo[0]:
            aasta += foo[1]
    aasta += isikukood[1:3]
    
    return paev + ". " + kuu + " " + aasta