def sünnikuupäev(i):
    kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august",
"september", "oktoober", "november", "detsember"]
    if int(i[0]) < 3:
        return i[5] + i[6] + ". " + kuud[int(i[3] + i[4]) - 1] + " 18" + i[1] + i[2]
    elif int(i[0]) < 5:
        return i[5] + i[6] + ". " + kuud[int(i[3] + i[4]) - 1] + " 19" + i[1] + i[2]
    elif int(i[0]) < 7:
        return i[5] + i[6] + ". " + kuud[int(i[3] + i[4]) - 1 ] + " 20" + i[1] + i[2]
    elif int(i[0]) < 9:
        return i[5] + i[6] + ". " + kuud[int(i[3] + i[4]) - 1 ] + " 21" + i[1] + i[2]
