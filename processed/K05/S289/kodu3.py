def moos(suured, väiksed, kogus):
    kasutatud = 0
    while kogus >= 5 and suured > 0:
        kogus -= 5
        suured -= 1
        kasutatud += 1
    while kogus > 0 and väiksed > 0:
        kogus -= 1
        väiksed -= 1
        kasutatud += 1
    if kogus > (5 * suured) + väiksed or kogus > väiksed:
        return(-1)
    else:
        return(kasutatud)

print(moos(5, 0, 3))




        
    
    
        
        

