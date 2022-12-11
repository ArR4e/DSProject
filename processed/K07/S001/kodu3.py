def sünnikuupäev(isik):
    kuu = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    kuu_number = 0
    sunnipaev = [0, "", 0]
    if isik[0] == "3" or isik[0] == "4":
        sunnipaev[2] += 1900
    elif isik[0] == "5" or isik[0] == "6":
        sunnipaev[2] += 2000
    sunnipaev[2] += int(isik[1])*10 + int(isik[2])
    kuu_number = int(isik[3])*10 + int(isik[4])
    sunnipaev[1] = kuu[kuu_number-1]
    sunnipaev[0] = int(isik[5])*10 + int(isik[6])
    return(str(sunnipaev[0]) + ". " + str(sunnipaev[1]) + " " + str(sunnipaev[2]))
    