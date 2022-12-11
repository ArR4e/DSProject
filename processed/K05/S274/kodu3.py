def moos(suured,väikesed,kogus):
    suurivaja = kogus // 5
    suurikasutada = min(suurivaja, suured)
    väikseidvaja = kogus - 5 * suurikasutada
    if väikseidvaja <= väikesed:
        return suurikasutada + väikseidvaja
    else:
        return -1
print(moos(3, 3, 8))

# tänan praktikumi plokkskeemi eest :)


