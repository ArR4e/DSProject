def sünnikuupäev(id_nr):
    
    kuud = ["jaanuar","01","veebruar","02","märts","03","aprill","04","mai","05","juuni","06","juuli","07","august","08","september","09","oktoober","10","november","11","detsember","12"]

    if id_nr[0] == "5" or id_nr[0] == "6":
         return id_nr[5:7]+". "+kuud[kuud.index(id_nr[3:5])-1]+" 20"+id_nr[1:3]
    if id_nr[0] == "4" or id_nr[0] == "3":
         return id_nr[5:7]+". "+kuud[kuud.index(id_nr[3:5])-1]+" 19"+id_nr[1:3]
    if id_nr[0] == "1" or id_nr[0] == "2":
         return id_nr[5:7]+". "+kuud[kuud.index(id_nr[3:5])-1]+" 18"+id_nr[1:3]
    
print(sünnikuupäev("19907062285"))