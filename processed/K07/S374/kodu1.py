def poisse_ja_tüdrukuid (jarjend):
    
    poisid = 0
    tudrukud = 0
    
    for n in jarjend:
        nimi = n.split()
        
        if nimi[-1] == 'P':
            poisid += 1
        else:
            tudrukud += 1
            
    return (poisid, tudrukud)