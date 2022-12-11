

def sünnikuupäev(ik):
    ikk = list(str(ik))
    
    if (ikk[0] == "1") or (ikk[0] == "2"):       
        ye = "18"                              
    if (ikk[0] == "3") or (ikk[0] == "4"):       
        ye = "19"                              
    if (ikk[0] == "5") or (ikk[0] == "6"):       
        ye = "20"                              
        
    ar = ikk[1] + ikk[2]
    
    month = ikk[3] + ikk[4]
    mmonth = "".join(month)
    if mmonth == "01":
        mmmonth = "jaanuar"
    if mmonth == "02":
        mmmonth = "veebruar"
    if mmonth == "03":
        mmmonth = "märts"
    if mmonth == "04":
        mmmonth = "aprill"
    if mmonth == "05":
        mmmonth = "mai"                
    if mmonth == "06":                 
        mmmonth = "juuni"
    if mmonth == "07":
        mmmonth = "juuli"
    if mmonth == "08":
        mmmonth = "august"
    if mmonth == "09":
        mmmonth = "september"
    if mmonth == "10":
        mmmonth = "oktoober"
    if mmonth == "11":
        mmmonth = "november"
    if mmonth == "12":
        mmmonth = "detsember"
        
    day = ikk[5] + ikk[6]
    dday = day + "."
    
    return(str(dday) + " " +  str(mmmonth) + " " + str(ye + ar))


    
        
    