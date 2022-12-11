def poisse_ja_tüdrukuid(list):
    poisid = 0
    tüdrukud = 0
    
    for element in list:
        if element[-1] == "P":
            poisid = poisid + 1
        else:
            tüdrukud = tüdrukud + 1
        
    return (poisid, tüdrukud)