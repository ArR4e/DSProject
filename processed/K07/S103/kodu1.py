def poisse_ja_tüdrukuid(järjend):
    m = 0
    n = 0
    for element in järjend:
        if element[-1] == "P":
            m += 1
        elif element[-1] == "T":
            n += 1
    return (m, n)