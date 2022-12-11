def moos(suur, väike, kg):
    karpe_vaja = 0
    while kg != 0:
        if kg >= 5 and suur > 0:
            kg -= 5
            suur -= 1
            karpe_vaja += 1
        elif kg != 0 and väike > 0:
            kg -= 1
            väike -= 1
            karpe_vaja += 1
        else:
            return -1
            break
    return karpe_vaja