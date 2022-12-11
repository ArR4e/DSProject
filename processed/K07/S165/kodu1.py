def poisse_ja_tüdrukuid(järjend):
    poisid = 0
    tüdrukud = 0
    
    for element in järjend:
        element = element.split()
        if element[-1] == "P":
            poisid += 1
        elif element[-1] == "T":
            tüdrukud += 1
        else:
            print("midagi on sisestatud valesti")
    ennik = (poisid,tüdrukud)
    return ennik


      
   
   
   
   