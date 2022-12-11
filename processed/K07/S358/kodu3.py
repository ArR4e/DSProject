def sünnikuupäev(ik):
    if ik[0] == "5" or ik[0] == "6":
        aasta = "20"+ik[1:3]
    elif ik[0] == "3" or ik[0] == "4":
        aasta = "19"+ik[1:3]
    elif ik[0] == "1" or ik[0] == "2":
        aasta = "18"+ik[1:3]
    kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    kuu = kuud[int(ik[3:5])-1]
    return ik[5:7]+". " + kuu + " " + aasta