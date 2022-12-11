month_list = ["0","jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]

def sünnikuupäev(isikukood):
    if int(isikukood[0]) < 3:
        aasta = '18' + isikukood[1:3]
    elif int(isikukood[0]) < 5:
        aasta = '19' + isikukood[1:3]
    else:
        aasta = '20' + isikukood[1:3]
    
    kuu_indeks = int(isikukood[3:5])
    kuu = month_list[kuu_indeks]
    kuu_as_string = str(kuu)
    
    paev = int(isikukood[5:7])
    paev_as_string = str(paev)
    return(paev_as_string+". "+ kuu+" "+ aasta)
    
sünnikuupäev('10104162735')
