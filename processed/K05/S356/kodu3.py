from math import floor
def moos (suurkarp,vaikekarp,moos):
    
    a = -1
        
    suurkarp_arv = moos / 5
    suurkarp_arv = floor(suurkarp_arv)
    vaikekarp_arv = moos % 5
    koguarv = suurkarp * 5 + vaikekarp
    
    if suurkarp_arv > suurkarp and vaikekarp_arv < vaikekarp and koguarv >= moos:
        vaikekarp_arv = (moos - suurkarp * 5)
        return(suurkarp + vaikekarp_arv)
    
    elif suurkarp_arv > suurkarp or vaikekarp_arv > vaikekarp or koguarv < moos:
        return(a)
    
    else:
        return(suurkarp_arv + vaikekarp_arv)
