def moos(a, b, c):
    if c >= 5:
        suur_moos = c // 5
        if suur_moos <= a:
              suured_karbid = suur_moos
        else:
            suured_karbid = a
        väike_moos = a - suured_karbid*5
        if väike_moos > b:
            return -1
        else:
            väiksed_karbid = väike_moos
        return suured_karbid + väiksed_karbid
    else:
        print("-1")