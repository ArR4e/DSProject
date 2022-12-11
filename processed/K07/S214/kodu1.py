def poisse_ja_tüdrukuid(järjend):
    m = 0
    n = 0
    for element in järjend:
        sugu = element[-1]
        if sugu == "P":
            m += 1
        elif sugu == "T":
            n += 1
    return (m, n)