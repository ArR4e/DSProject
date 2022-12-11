def poisse_ja_tüdrukuid(järjend):
    p = 0
    t = 0
    for element in järjend:
        sugu = element[-1]
        if sugu == "P":
            p += 1
        if sugu == "T":
            t += 1
    
    return (p, t)