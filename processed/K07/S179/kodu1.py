def poisse_ja_tüdrukuid(list):
    a=0
    b=0
    for rida in list:
        if rida[::-1][0] == "P":
            a += 1
        elif rida[::-1][0] == "T":
            b += 1
    return a,b