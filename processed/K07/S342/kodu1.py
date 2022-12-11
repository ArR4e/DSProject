def poisse_ja_tüdrukuid(järjend):
    m = 0
    n = 0
    for element in järjend:
        eraldi = element.split()
        for osa in eraldi:
            if osa == "P":
                m += 1
            elif osa == "T":
                n += 1
    väljund = (m, n)
    print(väljund)
    return väljund
