def moos(suuredKarbid, vaikesedKarbid, kogus):
    if suuredKarbid == 0 and vaikesedKarbid >= kogus:
        if int(kogus / 5) > suuredKarbid:
            print("siin1")
            vaikesedKarbid = kogus - (suuredKarbid * 5)
            return suuredKarbid + vaikesedKarbid
        else:
            suuredKarbid = int(kogus / 5)
            vaikesedKarbid = kogus - (suuredKarbid * 5)
            return suuredKarbid + vaikesedKarbid
        
    elif kogus - (suuredKarbid * 5) - (vaikesedKarbid * 1) > 0:
        print("siin1")
        return -1
    
    elif kogus % suuredKarbid > vaikesedKarbid:
        print("siin2")

        return -1
    
    elif kogus - (suuredKarbid * 5) < 0:
        if 5 + kogus - (suuredKarbid * 5) > vaikesedKarbid:
            return -1
    
    elif kogus - (suuredKarbid * 5) == 0:

        return suuredKarbid
    
    elif kogus == 0:
        return 0
   
    else:        
        if int(kogus / 5) > suuredKarbid:
            vaikesedKarbid = kogus - (suuredKarbid * 5)
            return suuredKarbid + vaikesedKarbid
        else:
            suuredKarbid = int(kogus / 5)
            vaikesedKarbid = kogus - (suuredKarbid * 5)
            return suuredKarbid + vaikesedKarbid

    
moos(4, 5, 0)




