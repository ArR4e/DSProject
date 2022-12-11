def moos(suur, väike, kg):
    if suur * 5 + väike >= kg:
        b = (kg - suur * 5)
        return suur + b
    else:
        print("-1")
