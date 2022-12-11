def poisse_ja_tüdrukuid(jarjend):
    count_poisid = 0
    count_tudrukud = 0
    for i in jarjend:
        if " P" in i:
            count_poisid = count_poisid + 1
        
        if " T" in i:
            count_tudrukud = count_tudrukud + 1

            
    andmed = (count_poisid, count_tudrukud)
    return andmed