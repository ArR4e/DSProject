isikukood = str(input("Sisesta oma isikukood: "))

def sünnikuupäev(isikukood):
    for element in isikukood:
        aasta = isikukood[0]
        aasta_lõpp = isikukood[1] + isikukood[2]
        if aasta == "6" or aasta == "5":
            aasta_lõpp = "20" + aasta_lõpp
        elif aasta == "1" or aasta == "2":
            aasta_lõpp = "18" + aasta_lõpp
        elif aasta == "3" or aasta == "4":
            aasta_lõpp = "19" + aasta_lõpp
        elif aasta == "7" or aasta == "8":
            aasta_lõpp = "21" + aasta_lõpp
            
        kuu_nimi = str(isikukood[3] + isikukood[4])
        if kuu_nimi == "12":
            kuu_nimi = "detsember"
        elif kuu_nimi == "11":
            kuu_nimi = "november"
        elif kuu_nimi == "10":
            kuu_nimi = "oktoober"
        elif kuu_nimi == "09":
            kuu_nimi = "september"
        elif kuu_nimi == "08":
            kuu_nimi = "august"
        elif kuu_nimi == "07":
            kuu_nimi = "juuli"
        elif kuu_nimi == "06":
            kuu_nimi = "juuni"
        elif kuu_nimi == "05":
            kuu_nimi = "mai"
        elif kuu_nimi == "04":
            kuu_nimi = "aprill"
        elif kuu_nimi == "03":
            kuu_nimi = "märts"
        elif kuu_nimi == "02":
            kuu_nimi = "veebruar"
        elif kuu_nimi == "01":
            kuu_nimi = "jaanuar"
        
        päev = isikukood[5] + isikukood[6]
        if isikukood[5] == "0":
            päev = isikukood[6]
            
        return (päev + "." + " " + kuu_nimi + " " + aasta_lõpp)
    

sünnikuupäev(isikukood)
print(sünnikuupäev(isikukood))

    