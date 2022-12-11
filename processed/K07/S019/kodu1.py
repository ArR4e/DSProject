def poisse_ja_tüdrukuid(järjend):
    m = 0
    n = 0
    for rida in järjend:
        if rida[-1] == "P":
            m += 1
            
        if rida[-1] == "T":
            n += 1
            
    return m, n

