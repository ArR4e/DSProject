def seosta_lapsed_ja_vanemad(f_lapsed, f_nimed):
    with open(f_nimed) as f:
        nimed = {isik[:11] : isik.strip()[12:] for isik in f.readlines()}
    with open(f_lapsed) as f:
        lapsed = f.readlines()
    return {nimed[i.strip()[12:]] : {nimed[j.strip()[:11]] for j in lapsed if j.strip()[12:] == i.strip()[12:]} for i in lapsed}