
sõne = []

def sünnikuupäev(isikukood):
    järjend = list(isikukood)
    päev = "".join(järjend[5:7])
    kuu_nr = järjend[3:5]
    if järjend[3] == "0" and järjend[4]=="1":
        kuu_sõnaga = "jaanuar"
    elif järjend[3] == "0" and järjend[4]=="2":
        kuu_sõnaga = "veebruar"
    elif järjend[3] == "0" and järjend[4]=="3":
        kuu_sõnaga = "märts"
    elif järjend[3] == "0" and järjend[4]=="4":
        kuu_sõnaga = "aprill"
    elif järjend[3] == "0" and järjend[4]=="5":
        kuu_sõnaga = "mai"
    elif järjend[3] == "0" and järjend[4]=="6":
        kuu_sõnaga = "juuni"
    elif järjend[3] == "0" and järjend[4]=="7":
        kuu_sõnaga = "juuli"
    elif järjend[3] == "0" and järjend[4]=="8":
        kuu_sõnaga = "august"
    elif järjend[3] == "0" and järjend[4]=="9":
        kuu_sõnaga = "september"
    elif järjend[3] == "1" and järjend[4]=="0":
        kuu_sõnaga = "oktoober"
    elif järjend[3] == "1" and järjend[4]=="1":
        kuu_sõnaga = "november"    
    elif järjend[3] == "1" and järjend[4]=="2":
        kuu_sõnaga = "detsember"
    
    aasta_lõpp = "".join(järjend[1:3])
 
    if järjend[0] == "1" or järjend[0] == "2":
            aasta = "18" + aasta_lõpp
    elif järjend[0] == "3" or järjend[0] == "4":
            aasta = "19" + str(aasta_lõpp)
    elif järjend[0] == "5" or järjend[0] == "6":
            aasta = "20" + aasta_lõpp
    return päev + "." + " " + kuu_sõnaga + " " + aasta
    

