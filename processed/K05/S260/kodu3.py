def moos(suur_karp,väike_karp,moos_kg):
    if moos_kg == 0:
        return 0
    if moos_kg > suur_karp*5 + väike_karp:
        return -1
    if (moos_kg - suur_karp*5) - väike_karp <= 0 and (moos_kg//5 <= suur_karp and moos_kg%5 <= väike_karp) or abs((moos_kg//5)-suur_karp)*5 <= väike_karp:
        return abs(((moos_kg//5) - ((moos_kg//5) - suur_karp)) + (moos_kg - ((moos_kg//5) - ((moos_kg//5) - suur_karp))*5))
        #return (suur_karp*(moos_kg//5))//5 + moos_kg - suur_karp*(moos_kg%5)
    if suur_karp == 0 and väike_karp > moos_kg:
        return moos_kg
    else:
        return -1

print(moos(1,0,5))