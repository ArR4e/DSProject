def sünnikuupäev(jrj):
    if jrj[3]+ jrj[4] == "01":
        kuu = "jaanuar"
    elif jrj[3]+ jrj[4] == "02":
        kuu = "veebruar"
    elif jrj[3]+ jrj[4] == "03":
        kuu = "märts"
    elif jrj[3]+ jrj[4] == "04":
        kuu = "aprill"
    elif jrj[3]+ jrj[4] == "05":
        kuu = "mai"
    elif jrj[3]+ jrj[4] == "06":
        kuu = "juuni"
    elif jrj[3]+ jrj[4] == "07":
        kuu = "juuli"
    elif jrj[3]+ jrj[4] == "08":
        kuu = "august"
    elif jrj[3]+ jrj[4] == "09":
        kuu = "september"
    elif jrj[3]+ jrj[4] == "10":
        kuu = "oktoober"
    elif jrj[3]+ jrj[4] == "11":
        kuu = "november"
    else:
        kuu = "detsember"
    if int(jrj[1]+ jrj[2]) < 22:
        aasta = "20" + jrj[1]+ jrj[2]
    elif int(jrj[0]) < 3:
        aasta = "18" + jrj[1]+ jrj[2]
    elif int(jrj[0]) > 4:
        aasta = "20" + jrj[1]+ jrj[2]
    else:
        aasta = "19" + jrj[1]+ jrj[2]
    return (jrj[5].replace("0","")+ jrj[6]+". " + kuu + " "+ aasta)