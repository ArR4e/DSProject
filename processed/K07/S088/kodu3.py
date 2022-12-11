def sünnikuupäev(i):
    i = list(i)
    if i[0] < "3":
        a = "18" + i[1] + i[2] 
    elif i[0] < "5":
        a = "19" + i[1] + i[2]   
    elif i[0] == "5" or i[0] == "6":
        a = "20" + i[1] + i[2]
        
    k = int((i[3] + i[4]))
    p = int((i[5] + i[6]))
    kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]  
    s = str(p) + ". " + kuud[k-1] + " " + str(a)
    return s