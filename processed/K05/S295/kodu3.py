def moos(suured, väikesed, kogus):
    mahub_suured = suured*5
    mahub_väiksesed = väikesed*1
    väikestearv = 0
    suurtearv= 0
    if kogus > (mahub_väiksesed + mahub_suured):
        print("-1")
    while not suured == 0:
        if kogus >= 0:
            suured = suured-1
            kogus = kogus-5
            suurtearv += 1
    while not väikesed == 0:
        if kogus >= 0:
            väikesed = väikesed-1
            kogus = kogus - 1
            väikestearv += 1
            if kogus == 0:
                print(suurtearv+väikestearv)
                                             
moos(6, 2, 32)