def poisse_ja_tüdrukuid(järjend):
    poisid = 0
    tüdrukud = 0
    for a in järjend:
        for b in a[-1]:
            if b == 'P':
                poisid += 1
            if b == 'T':
                tüdrukud += 1
    return (poisid, tüdrukud)