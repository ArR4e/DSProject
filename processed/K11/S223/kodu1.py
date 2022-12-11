def seosta_lapsed_ja_vanemad(lapsed, nimed):
    with open(lapsed, "r", encoding="utf-8") as f:
        list_lapsed = [x.strip().split() for x in f.readlines()]
    dict_lapsed = {x[1]:{y[0] for y in list_lapsed if y[1] == x[1]} for x in list_lapsed}
    with open(nimed, "r", encoding="utf-8") as f:
        dict_nimed = {x[:11]: x.strip()[12:] for x in f.readlines()}
    return {dict_nimed[x]: {dict_nimed[y] for y in dict_lapsed[x]} for x in dict_lapsed.keys()}
seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")