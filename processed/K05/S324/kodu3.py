def moos (suured_karbid, väiksed_karbid, kogus):
    
    kasutatud_suured = 0
    while kogus >= 5 and suured_karbid > kasutatud_suured:
        kogus = kogus - 5
        kasutatud_suured = kasutatud_suured + 1
    if väiksed_karbid >= kogus:
        return(kasutatud_suured + kogus)
    else:
        return(-1)
        

            
        
        
        

    
        
        