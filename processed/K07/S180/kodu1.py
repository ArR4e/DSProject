
def poisse_ja_tüdrukuid(järjend):
    poisside_arv = 0
    tüdrukute_arv = 0
    for sõne in järjend:
        if sõne[-1] == 'P':
            poisside_arv += 1
        elif sõne[-1] == 'T':
            tüdrukute_arv += 1
    return (poisside_arv, tüdrukute_arv)