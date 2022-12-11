def moos(suur, väike, moos):
    suured = suur
    väiksed = väike
    while moos != 0:
        if moos//5 and suur != 0:
            moos-=5
            suur-=1
        elif väike != 0:
            moos-=1
            väike-=1
        else:
            return -1
    return suured-suur+(väiksed-väike)

print(moos(5,5,0))