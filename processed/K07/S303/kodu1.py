def poisse_ja_tüdrukuid(järjend):
    tüdrukud = 0
    poisid = 0
    for elm in järjend:
        if elm[-1] == 'P':
            poisid += 1
        elif elm[-1] == 'T':
            tüdrukud += 1
    return (poisid, tüdrukud)