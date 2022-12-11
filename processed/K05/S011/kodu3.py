def moos(suured_karbid, väiksed_karbid, moos_kg):
    kasutatud_karbid = 0
    if moos_kg/(suured_karbid*5 + väiksed_karbid) != int() :
        return(-1)
    else:
        while suured_karbid>0 and suured_karbid*5 <= moos_kg:
            moos_kg = moos_kg-5
            suured_karbid = suured_karbid - 1
            kasutatud_karbid += 1
        while väiksed_karbid>0 and väiksed_karbid <= moos_kg:
            moos_kg -= 1
            väiksed_karbid -= 1
            kasutatud_karbid += 1
        return (kasutatud_karbid)
    
