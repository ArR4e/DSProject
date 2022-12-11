def poisse_ja_tüdrukuid(järjend):
    tüdrukud = 0
    poisid = 0
    for el in järjend:
        
        if el[-1] == "T":
            tüdrukud += 1
        else:
            poisid += 1
    print("("+str(poisid)+", "+str(tüdrukud)+")")