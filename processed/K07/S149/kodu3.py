def sünnikuupäev(id):
    id = str(id)
    kuud = ["Jaanuar", "Veebruar", "Märts", "Aprill", "Mai", "Juuni", "Juuli", "August", "September", "Oktoober", "November", "Detsember"]
    if int(id[0]) < 3:
        aasta = "18"
    elif int(id[0]) < 5:
        aasta = "19"
    else:
        aasta = "20"
    return id[5:7] + ". " + kuud[int(id[3:5]) - 1].lower() + " " + aasta + id[1:3]
print(sünnikuupäev(50012296043))