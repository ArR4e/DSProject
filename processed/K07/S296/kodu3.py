def sünnikuupäev(isik):
    sajand = isik[0]
    aasta_nr = str(isik[1]) + str(isik[2])
    kuu_nr = str(isik[3]) + str(isik[4])
    päev = str(isik[5]) + str(isik[6])
    if isik[5] == "0":
        päev = str(isik[6])
    if kuu_nr == "01":
        kuu = "jaanuar"
    if kuu_nr == "02":
        kuu = "veebruar"
    if kuu_nr == "03":
        kuu = "märts"
    if kuu_nr == "04":
        kuu = "aprill"
    if kuu_nr == "05":
        kuu = "mai"
    if kuu_nr == "06":
        kuu = "juuni"
    if kuu_nr == "07":
        kuu = "juuli"
    if kuu_nr == "08":
        kuu = "august"
    if kuu_nr == "09":
        kuu = "september"
    if kuu_nr == "10":
        kuu = "oktoober"
    if kuu_nr == "11":
        kuu = "november"
    if kuu_nr == "12":
        kuu = "detsember"
    if sajand == "1" or sajand == "2":
        aasta = 1800 + int(aasta_nr)
    if sajand == "3" or sajand == "4":
        aasta = 1900 + int(aasta_nr)
    if sajand == "5" or sajand == "6":
        aasta = 2000 + int(aasta_nr)
    if sajand == "7" or sajand == "8":
        aasta = 2100 + int(aasta_nr)
    return(päev + ". " + kuu + " " +str(aasta))
