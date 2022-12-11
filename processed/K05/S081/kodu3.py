def moos(a,b,c):
    suured = c//5
    if suured > a:
        väikesed = c - a*5
        if väikesed < b:
            return väikesed + a
        else:
            return -1
    else:
        väikesed = c-suured*5
        if väikesed > b:
            return -1
        else:
            return suured + väikesed