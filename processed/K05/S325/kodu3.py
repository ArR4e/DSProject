def moos(suured,väiksed,mass):
    karbid = 0
    try:
        while suured>0 and mass>=5:
            karbid+=1
            suured -=1
            mass -=5
        if mass>väiksed:
            int(üks)
        else:
            while väiksed>0 and mass>=1:
                karbid += 1
                väiksed -= 1
                mass -= 1
            return(karbid)
    except:
        return (-1)