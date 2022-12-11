def moos(suurolemas, väikeolemas, moos):
    suurvaja = moos//5
    if suurvaja > suurolemas:
        suurvaja=suurolemas
    väikevaja=moos-suurvaja*5
    if väikevaja > väikeolemas:
        return -1
    else:
        return suurvaja+väikevaja
    
