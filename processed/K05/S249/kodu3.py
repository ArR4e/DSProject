

def moos(suured, väiksed, kogus):
    suurivaja = kogus // 5
    suurikasutada = min(suurivaja, suured)
    väikseidvaja = kogus - suurikasutada * 5
    
    if väikseidvaja <= väiksed:
        return suurikasutada + väikseidvaja
    else:
        return -1