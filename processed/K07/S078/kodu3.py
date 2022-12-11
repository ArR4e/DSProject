def month_name (number):
    if number == "01":
        return "jaanuar"
    elif number == "02":
        return "veebruar"
    elif number == "03":
        return "märts"
    elif number == "04":
        return "aprill"
    elif number == "05":
        return "mai"
    elif number == "06":
        return "juuni"
    elif number == "07":
        return "juuli"
    elif number == "08":
        return "august"
    elif number == "09":
        return "september"
    elif number == "10":
        return "oktoober"
    elif number == "11":
        return "november"
    elif number == "12":
        return "detsember"

def sünnikuupäev(isik):
    päev = isik[5:7]
    kuu = month_name(isik[3:5])
    if  int(isik[0]) < 3:
        aasta = "18" + isik[1:3]
    elif 3 <= int(isik[0]) < 5:
        aasta = "19" + isik[1:3]
    elif 5 <= int(isik[0]) < 7:
        aasta = "20" + isik[1:3]
    return päev +". " + kuu + " " + aasta