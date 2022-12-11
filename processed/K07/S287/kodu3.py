def sünnikuupäev(isikukood):
    nrkood = str(isikukood)
    sünniaasta = 0
    sünnikuu = 0
    sünnipäev = 0
    kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    if nrkood[0] == "1" or nrkood[0] == "2":
        sünniaasta += 1800
    elif nrkood[0] == "3" or nrkood[0] == "4":
        sünniaasta += 1900
    elif nrkood[0] == "5" or nrkood[0] == "6":
        sünniaasta += 2000
    elif nrkood[0] == "7" or nrkood[0] == "8":
        sünniaasta += 2100
    else:
        print("error")
    
    sünniaasta += (int(nrkood[1]) * 10) + int(nrkood[2])
    sünnikuu += (int(nrkood[3]) * 10) + int(nrkood[4])
    sünnipäev += (int(nrkood[5]) * 10) + int(nrkood[6])
    
    return(f"{str(sünnipäev)}. {kuud[sünnikuu-1]} {str(sünniaasta)}")