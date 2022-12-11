def moos(suur_karp, väike_karp, moos_kg):
    kasutatud_karbid = 0
    while moos_kg >= 5 and suur_karp > 0:
        kasutatud_karbid += 1
        moos_kg = moos_kg - 5
        suur_karp = suur_karp - 1
    while moos_kg > 0 and väike_karp > 0:
        if väike_karp >= moos_kg:
            kasutatud_karbid += 1
            moos_kg = moos_kg - 1
            väike_karp = väike_karp - 1
        else:
            return -1
    return(kasutatud_karbid)
    
print(moos(2,6,14))