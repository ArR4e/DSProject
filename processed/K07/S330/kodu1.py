def poisse_ja_tüdrukuid(järjend):
    m = 0
    n = 0
    for el in järjend:
        if len(järjend)!= 0:
            if " P" in el:
                m += 1
            elif " T" in el:
                n += 1
    return (m, n)