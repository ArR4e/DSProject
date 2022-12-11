# <päev>. <kuu nimi> <aasta>
def sünnikuupäev(isikukood):
    number_1 = isikukood[0]
    if number_1 == "1" or number_1 == "2":
        synniaasta = 1800
    elif number_1 == "3" or number_1 == "4":
        synniaasta = 1900
    elif number_1 == "5" or number_1 == "6":
        synniaasta = 2000
    elif number_1 == "7" or number_1 == "8":
        synniaasta = 2100

    # 2 viimast aasta numbrit indexil 1 ja 2 [1:3] 
    synniaasta_lopp = isikukood[1:3]
    i_synniaasta_lopp = int(synniaasta_lopp)
    synniaasta_kokku = str(synniaasta + i_synniaasta_lopp)
    
    
    #  kuu nimi 
    kuu_number = isikukood[3:5]
    if kuu_number == "01":
        kuu_nimi = "jaanuar"
    elif kuu_number == "02":
        kuu_nimi = "veebruar"
    elif kuu_number == "03":
        kuu_nimi = "märts"
    elif kuu_number == "04":
        kuu_nimi = "aprill"
    elif kuu_number == "05":
        kuu_nimi = "mai"
    elif kuu_number == "06":
        kuu_nimi = "juuni"
    elif kuu_number == "07":
        kuu_nimi = "juuli"
    elif kuu_number == "08":
        kuu_nimi = "august"
    elif kuu_number == "09":
        kuu_nimi = "september"
    elif kuu_number == "10":
        kuu_nimi = "oktoober"
    elif kuu_number == "11":
        kuu_nimi = "november"
    elif kuu_number == "12":
        kuu_nimi = "detsember"
    
    # päev. [5:7]
    if isikukood[5] == "0":
        paev = isikukood[6:7]
    else:
        paev = isikukood[5:7]
    
    vastus = paev + '. ' + kuu_nimi + ' ' + synniaasta_kokku
    return vastus
    
print(sünnikuupäev("14501531215"))

