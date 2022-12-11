def moos(suured, väiksed, kogus):
    if kogus < 5 and väiksed >= kogus:
        return kogus
    if suured * 5 + väiksed < kogus:
        return -1
    else:
        while suured * 5 > kogus:
            suured -= 1
        vaja = kogus - (suured * 5)
        if väiksed >= vaja:
            return vaja + suured
        else:
            return -1
print(moos(5, 0, 3))
