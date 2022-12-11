def rek_abs(jär):
    if type(jär) != list:
        return abs(jär)
    else:
        uus_jär = []
        for el in jär:
            uus_jär.append(rek_abs(el))
        return uus_jär

            
    
    
    
    
    