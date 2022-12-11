def moos(arv_suurte, arv_väikeste, moosi):
    karpe = 0
    while moosi != 0:
        if arv_suurte != 0 and moosi - 5 >= 0:
            moosi -= 5
            arv_suurte -= 1
            karpe += 1
        if arv_väikeste !=0 and moosi - 1 >= 0:
            moosi -= 1
            arv_väikeste -= 1
            karpe += 1
        if arv_väikeste == 0 and 0 < moosi < 5 or arv_väikeste == 0 and arv_suurte == 0 and moosi > 0:
            return -1
    return karpe
