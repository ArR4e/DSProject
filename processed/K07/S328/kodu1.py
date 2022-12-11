def poisse_ja_tüdrukuid(järjend):
    m = 0
    n = 0
    for i in järjend:
        if i[-1] == "P":
            m += 1
        else:
            n += 1
    return (m, n)