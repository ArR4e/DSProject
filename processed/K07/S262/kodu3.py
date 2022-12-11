def sünnikuupäev(isikukood):
    ik = list(str(isikukood))
    vastus = ""
    vastus += ik[5]
    vastus += ik[6]
    vastus += ". "
    if ik[3] == "1" and ik[4] == "0":
        vastus += "oktoober "
    elif ik[3] == "1" and ik[4] == "1":
        vastus += "november "
    elif ik[3] == "1" and ik[4] == "2":
        vastus += "detsember "
    elif ik[4] == "1":
        vastus += "jaanuar "
    elif ik[4] == "2":
        vastus += "veebruar "
    elif ik[4] == "3":
        vastus += "märts "
    elif ik[4] == "4":
        vastus += "aprill "
    elif ik[4] == "5":
        vastus += "mai "
    elif ik[4] == "6":
        vastus += "juuni "
    elif ik[4] == "7":
        vastus += "juuli "
    elif ik[4] == "8":
        vastus += "august "
    else:
        vastus += "september "
    if ik[0] == "1" or ik[0] == "2":
        vastus += "18"
    elif ik[0] == "3" or ik[0] == "4":
        vastus += "19"
    elif ik[0] == "5" or ik[0] == "6":
        vastus += "20"
    vastus += ik[1]
    vastus += ik[2]
    return(vastus)
print(sünnikuupäev(34501234215))