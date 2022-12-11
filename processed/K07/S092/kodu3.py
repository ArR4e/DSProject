months = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]

def sünnikuupäev(isikukood):
    if int(isikukood[0]) == 1 or int(isikukood[0]) == 2:
        year = 1800
    elif int(isikukood[0]) == 3 or int(isikukood[0]) == 4:
        year = 1900
    elif int(isikukood[0]) == 5 or int(isikukood[0]) == 6:
        year = 2000
    elif int(isikukood[0]) == 7 or int(isikukood[0]) == 8:
        year = 2100

    year = year + int(isikukood[1]) * 10 + int(isikukood[2])
    month = int(isikukood[3]) * 10 + int(isikukood[4])
    month = months[month-1]
    date = int(isikukood[5]) * 10 + int(isikukood[6])
    
    return str(date) + ". " + str(month) + " " + str(year)
