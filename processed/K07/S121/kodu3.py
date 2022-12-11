def sünnikuupäev(id_code):
    _code = []
    aasta = ""
    kuud = ""
    paev = ""
    _code = list(id_code)
    if _code[0] == "3" or _code[0] == "4":
        aasta = 19
    elif _code[0] == "1" or _code[0] == "2":
        aasta = 18
    else:
        aasta = 20
    if _code[3] == "0" and _code[4] == "1":
        kuud = "jaanuar"
    elif _code[3] == "0" and _code[4] == "2":
        kuud = "veebruar"
    elif _code[3] == "0" and _code[4] == "3":
        kuud = "märts"
    elif _code[3] == "0" and _code[4] == "4":
        kuud = "aprill"
    elif _code[3] == "0" and _code[4] == "5":
        kuud = "mai" 
    elif _code[3] == "0" and _code[4] == "6":
        kuud = "juuni"    
    elif _code[3] == "0" and _code[4] == "7":
        kuud = "juuli"
    elif _code[3] == "0" and _code[4] == "8":
        kuud = "august"
    elif _code[3] == "0" and _code[4] == "9":
        kuud = "september"
    elif _code[3] == "1" and _code[4] == "0":
        kuud = "oktoober"
    elif _code[3] == "1" and _code[4] == "1":
        kuud = "november"
    elif _code[3] == "1" and _code[4] == "2":
        kuud = "detsember"
    aasta = str(aasta) + str(_code[1]) + str(_code[2])
    paev = str(_code[5]) + str(_code[6])
    return paev +". " + kuud + " " + aasta
print(sünnikuupäev('34501234215'))