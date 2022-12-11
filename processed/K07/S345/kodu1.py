def poisse_ja_tüdrukuid(järjend):
    m = 0
    n = 0
    for el in järjend:
        if len(järjend) == 0:
            return (m, n)
        elif el[-1] == "P":
            m += 1
        else:
            n += 1
    return (m, n)