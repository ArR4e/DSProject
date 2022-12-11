def moos(suured, väikesed, kogus):
    if type(kogus) != int or (kogus - (suured * 5 + väikesed)) > 0 or (kogus - int(kogus / 5) * 5 - väikesed) > 0:
        return -1
    else :
        arv = 0
        while kogus > 0:
            if kogus > 4 and suured > 0:
                kogus -= 5
                arv += 1
                suured -= 1
            elif kogus > 0:
                kogus -= 1
                arv += 1
                
        return arv