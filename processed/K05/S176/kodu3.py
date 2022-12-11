def moos(suuri_karpe, väikeseid_karpe, kogus):
    suure_mahutavus = 5
    väikese_mahutavus = 1
    suuri = 0
    väikeseid = 0
    kokku = 0
    while kogus >= 5:
        if suuri_karpe > 0:
            suuri += 1
            suuri_karpe -= 1
            kogus -= 5
        elif suuri_karpe == 0:
            break
    while 0 < kogus <= 5:
        if väikeseid_karpe > 0:
            väikeseid += 1
            väikeseid_karpe -= 1
            kogus -= 1
        elif väikeseid_karpe == 0:
            break
    if suuri * suure_mahutavus + väikeseid * väikese_mahutavus < suuri * suure_mahutavus + väikeseid * väikese_mahutavus + kogus:
        kokku = -1
    else:
        kokku = suuri + väikeseid
    return kokku