def sünnikuupäev(x):
    s = []
    for el in x:
        s += el
    if s[0] == "2" or s[0] == "1":
        aastaalgus = "18"
    elif s[0] == "3" or s[0] == "4":
        aastaalgus = "19"
    elif s[0] == "6" or s[0] == "5":
        aastaalgus = "20"
    aasta = aastaalgus + str(s[1]+s[2])
    if s[3] == "0" and s[4] == "1":
        kuu = "jaanuar"
    if s[3] == "0" and s[4] == "2":
        kuu = "veebruar"
    if s[3] == "0" and s[4] == "3":
        kuu = "märts"
    if s[3] == "0" and s[4] == "4":
        kuu = "aprill"
    if s[3] == "0" and s[4] == "5":
        kuu = "mai"
    if s[3] == "0" and s[4] == "6":
        kuu = "juuni"
    if s[3] == "0" and s[4] == "7":
        kuu = "juuli"
    if s[3] == "0" and s[4] == "8":
        kuu = "august"
    if s[3] == "0" and s[4] == "9":
        kuu = "september"
    if s[3] == "1" and s[4] == "0":
        kuu = "oktoober"
    if s[3] == "1" and s[4] == "1":
        kuu = "november"
    if s[3] == "1" and s[4] == "2":
        kuu = "detsember"
    päev = s[5]+s[6]+"."
    return päev+" "+kuu+" "+aasta